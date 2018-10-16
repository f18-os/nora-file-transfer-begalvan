#thread server file

import socket
import os
from _thread import *
import threading 

num_of_clients = 5 #listen to up to 5 clients
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 50001))
server.listen(num_of_clients) 
text_file = 'client_' + str(1) + '.txt'
lock = threading.Lock() #initialize lock

i = 1
while i <= num_of_clients:
    c, addr = server.accept()
    lock.acquire()
    print("\nconnection successful with client " +
            str(i) + str(addr) + "\n")
    text_file = 'client_' + str(i) + '.txt'

    # Receive, output and save file
    with open(text_file, "wb") as fw: #opens file and returns stream
        print("Receiving..")
        while True:
            print('receiving')
            data = c.recv(100) #receive up to 100 bytes from socket
            if data == b'start': #bytes-start
                continue
            elif data == b'end':
                print('Breaking from file write')
                break
            else:
                decoded_data = data.decode("utf-8")
                if not decoded_data:
                    print("\nconnection with client " + str(i) + " broken\n")
                    print("  CLIENT " + str(i) + " -> " + decoded_data)
                    break