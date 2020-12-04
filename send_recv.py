import socket
import tqdm
import os
import argparse

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 4 #4KB

def send_file(filename, s, TYPE='comp'):

	filesize = os.path.getsize(filename)
	print(filesize)

	if(TYPE[0:2]=="img"):
		pass
		# quality=

	s.send(f"{filename}{SEPARATOR}{filesize}{SEPARATOR}{TYPE}".encode())
	# progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024)
	with open(filename, "rb") as f:
		while True:
			# read the bytes from the file
			print("send_test")
			bytes_read = f.read(BUFFER_SIZE)
			print(bytes_read)
			if not bytes_read:
				s.sendall(bytes_read)
				# file transmitting is done
				break
			# we use sendall to assure transimission in 
			# busy networks
			s.sendall(bytes_read)
	
def recv_file(recv_path, client_socket):
	# receive the file infos
	# receive using client socket, not server socket
	received = client_socket.recv(BUFFER_SIZE).decode()
	filename, filesize, method = received.split(SEPARATOR)
	# remove absolute path if there is
	filename = os.path.basename(filename)
	# convert to integer
	filesize = int(filesize)
	# start receiving the file from the socket
	# and writing to the file stream

	print(filename, filesize)
	with open(recv_path, "wb") as f:
		while True:
			# read 1024 bytes from the socket (receive)
			print("recv_test")
			bytes_read = client_socket.recv(BUFFER_SIZE)
			print(bytes_read)
			if bytes_read == b'':    
				# nothing is received
				# file transmitting is done
				break
			# write to the file the bytes we just received
			f.write(bytes_read)

	return method