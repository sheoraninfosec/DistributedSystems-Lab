#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

int main() {

    int sockfd;
    struct sockaddr_in serv_addr;
    char buffer[1024];

    sockfd = socket(AF_INET, SOCK_STREAM, 0);

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(12345);
    serv_addr.sin_addr.s_addr = inet_addr("127.0.0.1");

    connect(sockfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr));

    printf("connected to server 127.0.0.1 : 12345\n");

    while (1) {
        // Client writes first
        printf("client: ");
        fgets(buffer, sizeof(buffer), stdin);
        buffer[strcspn(buffer, "\n")] = '\0';

        write(sockfd, buffer, strlen(buffer));

        if (strcmp(buffer, "exit") == 0)
            break;

        memset(buffer, 0, sizeof(buffer));

        // Read server reply
        read(sockfd, buffer, sizeof(buffer));
        printf("server: %s\n", buffer);

        if (strcmp(buffer, "exit") == 0)
            break;
    }

    close(sockfd);
    return 0;
}
