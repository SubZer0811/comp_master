from easygui import *
import huffman.compressor
import socket
import send_recv
import time

HOST = '127.0.0.1'
PORT = 45000
SEPARATOR = "<SEPARATOR>"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# sock.setblocking(False)
def compress():
	print("Inside Compress")

	choices = ["Text", "Image", "Video", "Audio", "Multiple Files"]
  
	# mesaage / question to be asked
	msg = "Select any one option"
	
	# opening a choice box using our msg and choices 
	# reply = choicebox(msg, choices = choices)
	reply = "Text"

	if(reply == "Text"):
		compress_text()
	if(reply == "Image"):
		compress_image()

def compress_text():

	# file = fileopenbox()
	choices = ["Huffman", "Shannon-Fano", "LZW", "RLE"]
  
	# mesaage / question to be asked
	msg = "Select compression Algorithm"
	
	# opening a choice box using our msg and choices 
	# method = choicebox(msg, choices = choices)
	method = "Huffman"
	file = "source.txt"

	send_recv.send_file(file, sock, "comp_" + method)
	time.sleep(1)
	send_recv.recv_file("compressessasads", sock)

def decompress_text():

	file = fileopenbox()
	choices = ["Huffman", "Shannon-Fano", "LZW", "RLE"]
  
	# mesaage / question to be asked
	msg = "Select decompression Algorithm"
	
	# opening a choice box using our msg and choices 
	method = choicebox(msg, choices = choices)
	send_recv.send_file(file, sock, "decomp" + method)
	# send_recv.recv_file('comp', sock)

def compress_image():

	file = fileopenbox()
	text="Enter quality factor 10 - 100"
	title="Image compression"
	d_int = 75
	lower = 10
	upper=100

	output=integerbox(text,title,d_int,lower,upper)
	send_recv.send_file(file,sock,"img"+"{SEPARATOR}"+str(output))


def decompress():

	choices = ["Text", "Archive"]
  
	# mesaage / question to be asked
	msg = "Select any one option"
	
	# opening a choice box using our msg and choices 
	reply = choicebox(msg, choices = choices)

	if(reply == "Text"):
		decompress_text()
	if(reply == "Text"):
		decompress_archive()

def compress_multiple_files():

	openfiles = fileopenbox("Welcome", "COPR", filetypes= "*.txt", multiple=True)
	choices = ["bz2", "gz", "xz"]
	msg = "Select any one option"
	reply = choicebox(msg, choices = choices)

	if(reply == "bz2"):
		compress_multiple_files_bz2()
	if(reply == "gz"):
		compress_multiple_files_gz()
	if(reply == "xz"):
		compress_multiple_files_xz()
	
# def decompress_archive():



if __name__ == "__main__":
	
	# message to be displayed  
	text = "Select on of the following options:"
	
	# window title 
	title = "Window Title GfG"
	
	# button list 
	button_list = []
	
	# button 1 
	button1 = "Compress"
	
	# second button 
	button2 = "Decompress"
	
	# appending button to the button list 
	button_list.append(button1)
	button_list.append(button2)
	
	# creating a button box 
	# output = buttonbox(text, title, button_list)
	output = "Compress"
	
	if(output == "Compress"):
		compress()
	elif(output == "Decompress"):
		decompress()

	sock.close()