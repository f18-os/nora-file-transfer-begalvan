# File Transfer-Threaded Lab

CS 4375

Directory `thread-lab` includes: 

fileThreadClient.py and fileThreadServer.py.

*   `fileThreadClient.py` transfers a file to the server using port 50001

*   `fileThreadServer.py` receives a file from client -up to 100 bytes from the socket at a time- listening on port 50001

These files run on Cygwin Python Version 3

To run files: 

* 1. Open fileServer.py:

        python3 fileServer.py

* 2. Open fileClient.py:

        python3 fileClient.py
        
form socket and will write data to create new file

steps:
lock=threading.lock() - first
lock.aquire - second
lock.release() - third

Please refer to COLLABORATORS file for information on collaboration and external resources.