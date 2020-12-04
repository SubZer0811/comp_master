import socket
import sys
import send_recv

HOST = '127.0.0.1'
PORT = 45000

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

send_recv.send_file("../theory/CN-Master-Slides.pdf", sock)

sock.close()