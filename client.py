from easygui import *
import huffman.compressor
import socket
from helpers import send_recv
import time
import config
from helpers import con

HOST = '34.72.59.38'
PORT = 47000

SEPARATOR = "<SEPARATOR>"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((config.HOST,config.PORT))

def compress():
	print("Inside Compress")

	choices = ["Text", "Image", "Video", "Audio", "Multiple Files"]
  
	# mesaage / question to be asked
	msg = "Select any one option"
	
	# opening a choice box using our msg and choices 
	reply = choicebox(msg, choices = choices)

	if(reply == "Text"):
		compress_text()
	elif(reply == "Image"):
		compress_image()
	elif(reply == "Video"):
		compress_vid()
	elif(reply == "Multiple Files"):
		compress_multiple_files()
	elif(reply == "Audio"):
		compress_aud()

def compress_text():

	file = fileopenbox(filetypes=['All files','*'])
	choices = ["Huffman", "Shannon-Fano", "LZW", "RLE"]
	
	# mesaage / question to be asked
	msg = "Select compression Algorithm"
	
	# opening a choice box using our msg and choices 
	method = choicebox(msg, choices = choices)
	send_recv.send_file(file, sock, "comp_" + method)
	time.sleep(1)
	save_file=filesavebox()
	send_recv.recv_file(save_file+"."+method[:3].lower(), sock)

def decompress_text():

	file = fileopenbox()
	choices = ["Huffman", "Shannon-Fano", "LZW", "RLE"]
  
	# mesaage / question to be asked
	msg = "Select decompression Algorithm"
	
	# opening a choice box using our msg and choices 
	method = choicebox(msg, choices = choices)
	send_recv.send_file(file, sock, "decomp_" + method)
	save_file=filesavebox()
	send_recv.recv_file(save_file, sock)


def compress_image():

	file = fileopenbox()
	text="Enter quality factor 10 - 100"
	title="Image compression"
	d_int = 75
	lower = 10
	upper=100
	output=integerbox(text,title,d_int,lower,upper)
	send_recv.send_file(file,sock,"img"+"_"+str(output))
	save_file=filesavebox()
	send_recv.recv_file(save_file, sock)

def compress_vid():
	file = fileopenbox()
	send_recv.send_file(file,sock,"vid")
	save_file=filesavebox()
	send_recv.recv_file(save_file, sock)

def compress_aud():
	file = fileopenbox()
	send_recv.send_file(file,sock,"aud")
	save_file=filesavebox()
	send_recv.recv_file(save_file, sock)

def decompress():

	choices = ["Text", "Archive"]
	# mesaage / question to be asked
	msg = "Select any one option"
	# opening a choice box using our msg and choices 
	reply = choicebox(msg, choices = choices)
	if(reply == "Text"):
		decompress_text()
	if(reply == "Archive"):
		decompress_archive()

def compress_multiple_files():

	file_list = fileopenbox(multiple=True)
	choices = ["bz2", "gz", "xz"]
	msg = "Select any one option"
	mode = choicebox(msg, choices = choices)
	send_recv.send_multiple_files(file_list, sock, f"multi_{mode}")
	save_dir=diropenbox()
	send_recv.recv_file(save_dir+'/compressed.tar.'+mode, sock)
	
def decompress_archive():
	file = fileopenbox()
	send_recv.send_file(file,sock,"decomp_archive")
	send_recv.recv_file('', sock)

if __name__ == "__main__":
	
	# message to be displayed  
	text = "Select one of the following options:"
	
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