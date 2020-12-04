import socket
import send_recv
import huffman.compressor
import lzw.compressor
import shannon.compressor
# import rle.compress

HOST = '127.0.0.1'
PORT = 45000

s=socket.socket()

s.bind((HOST,PORT))

s.listen(1)

(client_socket,address)=s.accept()

method = send_recv.recv_file("./recvd", client_socket)

if(method == "Huffman"):
	comp_file = huffman.compressor.compress("./recvd",".")
if(method == "Shannon-fano"):
    comp_file = shannon.compressor.compress("./recvd",".")
if(method == "LZW"):
    comp_file = lzw.compressor.compress("./recvd",".")
if(method == "RLE"):
	comp_file = rle.compressor.compress()

s.close()