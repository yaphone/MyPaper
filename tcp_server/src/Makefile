
tcp_server: tcp_server.o
	$(CC) $(LDFLAGS) tcp_server.o -o tcp_server
tcp_server.o: tcp_server.c
	$(CC) $(CFLAGS) -c tcp_server.c
clean:
	rm *.o tcp_server
