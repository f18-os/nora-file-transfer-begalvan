# File Transfer-Threaded Lab

Directory `lab` includes: 
fileThreadedClient.py, fileThreadedServer.py, and send_file.txt

*   `fileThreadedClient.py` transfers a file to the server using port 50001

*   `fileThreadedServer.py` receives a file from client -up to 100 bytes from the socket at a time- listening on port 50001

These files run on Cygwin Python Version 3

To run files: 

* 1. Open fileServer.py:

        python3 fileServer.py

* 2. Open fileClient.py (up to 5 clients):

        python3 fileClient.py

    client will immediately send send_file.txt to server, server will receive up to 100 bytes at a time
form socket and will write data to create new file

steps:
lock=threading.lock() - first
lock.aquire - second
lock.release() - third

