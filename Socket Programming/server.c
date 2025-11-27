#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main() {

    int sockfd, newsockfd;
    struct sockaddr_in serv_addr, cli_addr;
    char buffer[1024];
    socklen_t clilen;

    sockfd = socket(AF_INET, SOCK_STREAM, 0);

    // --- FIX: allow immediate reuse of port ---
    int opt = 1;
    setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
    serv_addr.sin_port = htons(12345);

    bind(sockfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr));
    listen(sockfd, 5);

    printf("server listening on 127.0.0.1 : 12345\n");

    clilen = sizeof(cli_addr);
    newsockfd = accept(sockfd, (struct sockaddr*)&cli_addr, &clilen);

    while (1) {
        memset(buffer, 0, sizeof(buffer));

        // Receive from client
        int n = read(newsockfd, buffer, sizeof(buffer));
        if (n <= 0) break;

        printf("client: %s\n", buffer);

        if (strcmp(buffer, "exit") == 0)
            break;

        // Server responds
        printf("server: ");
        fgets(buffer, sizeof(buffer), stdin);
        buffer[strcspn(buffer, "\n")] = '\0';

        write(newsockfd, buffer, strlen(buffer));

        if (strcmp(buffer, "exit") == 0)
            break;
    }

    close(newsockfd);
    close(sockfd);

    return 0;
}
