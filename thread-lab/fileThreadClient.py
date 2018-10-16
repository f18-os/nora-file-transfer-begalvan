#threaded client file

import socket
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 50001))

text_file = 'send_file.txt'

def send_file():
    with open(text_file, 'rb') as fs:
        sock.send(b'start')
        while True:
            data = fs.read(1024)
            print('Sending data', data.decode('utf-8'))
            sock.send(data)
            print('Sent data', data.decode('utf-8'))
            if not data:
                print("File is empty now!")
                print('Breaking from sending data')
                break
        sock.send(b'end')
        fs.close()