#include <netdb.h>
#include <sys/socket.h>
#include <errno.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define SERVER_PORT  8000
#define MAX_CLIENT_NUM  10

int main()
{
    int socketfd;
    socketfd = socket(AF_INET, SOCK_STREAM, 0);

    if(socketfd==-1)
    {
        printf("errorno=%d", errno);
        exit(1);
    }
    else
    {
        printf("socket create successfully\n");
    }

    struct sockaddr_in sa;
    bzero(&sa, sizeof(sa));
    sa.sin_family = AF_INET;
    sa.sin_port = htons(SERVER_PORT);
    sa.sin_addr.s_addr = htons(INADDR_ANY);
    bzero(&(sa.sin_zero), 8);

    if (bind(socketfd, (struct socketfd *)&sa, sizeof(sa))!=0)
    {
        printf("bind failed");
        printf("errorno=%d", errno);
        exit(1);
    }
    else
    {
        printf("bind successfully\n");
    }

    //listen
    if(listen(socketfd, MAX_CLIENT_NUM)!=0)
    {
        printf("listen error");
        exit(1);
    }
    else
    {
        printf("listen successfully\n");
    }

    int clientfd;
    struct sockaddr_in clientAdd;
    char buff[101];
    socklen_t len = sizeof(clientAdd);
    int closing = 0;
    while( closing == 0  && (clientfd = accept(socketfd, (struct sockaddr *)&clientAdd, &len)) >0 )
    {
        int n;
        while((n=recv(clientfd, buff, 100, 0)) > 0)
        {
            printf("number of receive bytes=%d \n", n);
            write(STDOUT_FILENO, buff, n);
            buff[n] = '\n';
            if(strcmp(buff, "quit")==0)
            {
                break;
            }
            else if(strcmp(buff, "close") == 0)
            {
                closing = 1;
                printf("server is closing");
                break;
            }
        }
        close(clientfd);
    }
    close(socketfd);

    return 0;

}
