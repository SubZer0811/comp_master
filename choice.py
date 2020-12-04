from easygui import *
import huffman.compressor
import socket
import send_recv

HOST = '127.0.0.1'
PORT = 45000
SEPARATOR = "<SEPARATOR>"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

def compress():
	print("Inside Compress")

	choices = ["Text", "Image", "Video", "Audio", "Multiple Files"]
  
	# mesaage / question to be asked
	msg = "Select any one option"
	
	# opening a choice box using our msg and choices 
	reply = choicebox(msg, choices = choices)

	if(reply == "Text"):
		compress_text()

def compress_text():

	file = fileopenbox()
	choices = ["Huffman", "Shannon-Fano", "LZW", "RLE"]
  
	# mesaage / question to be asked
	msg = "Select compression Algorithm"
	
	# opening a choice box using our msg and choices 
	method = choicebox(msg, choices = choices)
	send_recv.send_file(file, sock, method)

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
	print("Inside Decompress")
	pass

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
	output = buttonbox(text, title, button_list)
	
	if(output == "Compress"):
		compress()
	elif(output == "Decompress"):
		decompress()

	sock.close()