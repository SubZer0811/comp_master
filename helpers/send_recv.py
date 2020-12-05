import socket
import tqdm
import os
import argparse
import time

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 4 #4KB

def send_file(filename, s, TYPE='comp'):

	if(TYPE=='archive'):
		file_list = ["./archive/"+f for f in os.listdir('./archive/')]
		send_multiple_files(file_list, s)
		return
		
	print(f"Sending File: {filename}")
	filesize = os.path.getsize(filename)
	time.sleep(1)
	# if(TYPE[0:2]=="img"):
	# 	pass

	s.send(f"{filename}{SEPARATOR}{filesize}{SEPARATOR}{TYPE}".encode('utf-8'))

	print(s.recv(8))
	print("SENT HEADER")
	with open(filename, "rb") as f:
		while True:
			bytes_read = f.read(1)
			if not bytes_read:
				s.send(b'\x00')
				break
			s.send(bytes_read)
		f.close()
	print("Completed Sending")


def recv_file(recv_path, client_socket):

	# print("Receiving file")
	# received = client_socket.recv(BUFFER_SIZE)
	# recv2 = received
	# size = len(received)
	# print(f"received: {received}")

	# recv2 = str(recv2)[2:-1]
	# recv2 = recv2.split(SEPARATOR)
	# (filename, filesize, method) = recv2[:3]
	# filename = os.path.basename(filename)
	# filesize = int(filesize)
	count = 0
	tar_mode=''
	# print(f'Filename: {filename}\nFilesize: {filesize}')
	# print(f'This is what is recvd: {recv2}')
	received = client_socket.recv(BUFFER_SIZE)
	print(received)
	received = received.decode()
	print(received)
	filename, filesize, method = received.split(SEPARATOR)
	# remove absolute path if there is
	filename = os.path.basename(filename)
	# convert to integer
	filesize = int(filesize)

	client_socket.send("ack".encode('utf-8'))

	if(method[:6]=="multi_"):
		if (not os.path.isdir("./archive/")):
			os.mkdir("./archive/")
		else:
			for f in os.listdir('./archive/'):
				os.remove("./archive/"+f)
		recv_multiple_files("./archive/", client_socket, filesize)
		return method

	if(method=="decomp_archive"):
		tar_mode="_"+filename.split('.')[-1]

	with open(recv_path, "wb") as f:
		while True:
			bytes_read = client_socket.recv(1)
			count += 1
			if count == filesize+1:
				break
			f.write(bytes_read)
		f.close()

	return method+tar_mode

def send_multiple_files(file_list, s,TYPE="multi_"):

	# TYPE='multi_'
	print(f"Files to be sent:"+str(file_list)[1:-1])
	n=str(len(file_list))
	s.send((str(file_list)+f"{SEPARATOR}{n}{SEPARATOR}{TYPE}").encode('utf-8'))
	print(s.recv(8))
	print("SENT HEADER")

	for filename in file_list:
		print(f"Sending File: {filename}")
		filesize = os.path.getsize(filename)
		s.send((filename+SEPARATOR+str(filesize)).encode('utf-8'))
		print(s.recv(8))
		# filesize = os.path.getsize(filename)
		time.sleep(1)

		with open(filename, "rb") as f:
			while True:
				bytes_read = f.read(1)
				if not bytes_read:
					s.send(b'\x00')
					break
				s.send(bytes_read)
			f.close()

		print(f"Completed Sending {filename}")

def recv_multiple_files(recv_path, client_socket, n):
	for i in range(n):
		received = client_socket.recv(BUFFER_SIZE)
		print(received)
		received = received.decode()
		print(received)
		filename, filesize = received.split(SEPARATOR)
		# remove absolute path if there is
		filesize = int(filesize)
		filename = os.path.basename(filename)
		client_socket.send("ack".encode('utf-8'))
		count = 0
		with open(recv_path+filename, "wb") as f:	
			while True:
				bytes_read = client_socket.recv(1)
				count += 1
				if count == filesize+1:
					break
				f.write(bytes_read)
			f.close()
