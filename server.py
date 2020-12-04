import socket
import send_recv
import huffman.compressor
import lzw
import shannon
import rle
HOST = '127.0.0.1'
PORT = 45000

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST,PORT))

s.listen(1)
(client_socket,address)=s.accept()

# s.setblocking(False)
method = send_recv.recv_file("./recvd", client_socket)
result = ''
if(method[:5] == "comp_"):
	
	if(method[5:] == "Huffman"):
		result = huffman.compressor.compress("./recvd",".")
	if(method[5:] == "Shannon-Fano"):
		result = shannon.compressor.compress("./recvd",".")
	if(method[5:] == "LZW"):
		result = lzw.compressor.compress("./recvd",".")
	if(method[5:] == "RLE"):
		result = rle.compressor.compress("./recvd")

# def compress(tar_file, members, comp_mode):
# def decompress(tar_file, path, comp_mode, members=None):
	

else:

	if(method[7:] == "Huffman"):
		result = huffman.decompressor.decompress("./r",".")
	if(method[7:] == "Shannon-Fano"):
		result = shannon.decompressor.decompress("./recvd",".")
	if(method[7:] == "LZW"):
		result = lzw.decompressor.decompress("./recvd",".")
	if(method[7:] == "RLE"):
		print("asdf")
		result = rle.decompressor.decompress("./recvd")

send_recv.send_file(result, client_socket)


# send_recv.send_file()

s.close()