#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <unistd.h>

#define SHM_SIZE 1024

struct shmseg {
    int shm_written;
    char buffer[SHM_SIZE];
};

int main() {
    key_t key = ftok("shmfile", 65);
    int shmid = shmget(key, sizeof(struct shmseg), 0666 | IPC_CREAT);

    if (shmid < 0) {
        perror("shmget failed");
        exit(1);
    }

    pid_t pid = fork();

    if (pid < 0) {
        perror("fork failed");
        exit(1);
    }
    else if (pid == 0) {
        sleep(1);
        struct shmseg *shm = (struct shmseg*) shmat(shmid, NULL, 0);

        if (shm == (void *) -1) {
            perror("shmat failed");
            exit(1);
        }

        while (1) {
            if (shm->shm_written == 1) {
                printf("Child read: %s\n", shm->buffer);
                shm->shm_written = 0;
            }

            if (strcmp(shm->buffer, "exit") == 0) {
                break;
            }

            sleep(1);
        }

        shmdt(shm);
    }
    else {
        struct shmseg *shm = (struct shmseg*) shmat(shmid, NULL, 0);

        if (shm == (void *) -1) {
            perror("shmat failed");
            exit(1);
        }

        char input[SHM_SIZE];
        shm->shm_written = 0;

        while (1) {
            printf("Parent: Enter message (type 'exit' to quit): ");
            fgets(input, SHM_SIZE, stdin);
            input[strcspn(input, "\n")] = '\0';

            strcpy(shm->buffer, input);
            shm->shm_written = 1;

            if (strcmp(input, "exit") == 0) {
                break;
            }
        }

        shmdt(shm);
        shmctl(shmid, IPC_RMID, NULL);
    }

    return 0;
}
