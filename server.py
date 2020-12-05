import socket
import os
import sys
import subprocess
from helpers import send_recv
import huffman.compressor
import lzw.compressor
import shannon.compressor
import rle.compressor
import huffman.decompressor
import lzw.decompressor
import shannon.decompressor
import rle.decompressor
import tar.tar
from helpers.img_com import compressMe
import config
from helpers import con

HOST = '127.0.0.1'
PORT = 45000

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((config.HOST,config.PORT))

s.listen(1)
(client_socket,address)=s.accept()

# s.setblocking(False)
method = send_recv.recv_file("./recvd", client_socket)
print(method)
result=''

if(method[0:3]=="img"):
	method,quality=method.split("_")
	print(quality)
	print("image comp")
	result = compressMe("./recvd",False,int(quality))
	print(result)
elif(method[0:3]=="vid"):
	ip="./recvd"
	result="./compressed.mp4"
	subprocess.run('ffmpeg -i '+ip+' -vcodec libx265 -crf 28 '+result,shell=True) 

elif(method[0:3] == "aud"):
	ip="./recvd"
	result="./compressed.mp3"
	subprocess.run('ffmpeg -i '+ip+' -map 0:a:0 -b:a 96k '+result,shell=True) 
	
elif(method[:5] == "comp_"):
	
	if(method[5:] == "Huffman"):
		result = huffman.compressor.compress("./recvd",".")
	if(method[5:] == "Shannon-Fano"):
		result = shannon.compressor.compress("./recvd",".")
	if(method[5:] == "LZW"):
		result = lzw.compressor.compress("./recvd",".")
	if(method[5:] == "RLE"):
		result = rle.compressor.compress("./recvd")		

elif(method[:6] == "multi_"):
	result = tar.tar.compressor("./archive.tar."+method[6:],method[6:])
	# exit(0)

# def compress(tar_file, members, comp_mode):
# def decompress(tar_file, path, comp_mode, members=None):
	

else:

	if(method[7:] == "Huffman"):
		result = huffman.decompressor.decompress("./recvd",".")
	if(method[7:] == "Shannon-Fano"):
		result = shannon.decompressor.decompress("./recvd",".")
	if(method[7:] == "LZW"):
		result = lzw.decompressor.decompress("./recvd",".")
	if(method[7:] == "RLE"):
		print("asdf")
		result = rle.decompressor.decompress("./recvd",".")
	if(method[7:15] == "archive_"):
		print("HERE!!")
		print(f"METHOD = {method}\n{method[15:]}")
		result = tar.tar.decompressor("./recvd","./archive/",method[15:])
		send_recv.send_file(result, client_socket,"archive")
		os.system("rm -r ./archive")
		s.close()
		exit(0)

send_recv.send_file(result, client_socket)

os.system("rm ./recvd")
os.system("rm ./" + result)

s.close()
