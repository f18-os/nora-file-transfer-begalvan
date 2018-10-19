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

fileThreadServer.py can listen to up to 5 clients and will run following these steps:

* 1. lock = threading.lock() - first lock is initialized
* 2. lock.aquire
* 3. lock.release()

A primitive lock is in one of two states, “locked” or “unlocked”. It is created in the unlocked state. It has two basic methods, acquire() and release(). When the state is unlocked, acquire() changes the state to locked and returns immediately. When the state is locked, acquire() blocks until a call to release() in another thread changes it to unlocked, then the acquire() call resets it to locked and returns. The release() method should only be called in the locked state; it changes the state to unlocked and returns immediately. 

When more than one thread is blocked in acquire() waiting for the state to turn to unlocked, only one thread proceeds when a release() call resets the state to unlocked; which one of the waiting threads proceeds is not defined, and may vary across implementations.


Please refer to COLLABORATORS file for information on collaboration and external resources.