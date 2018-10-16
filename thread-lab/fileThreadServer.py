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