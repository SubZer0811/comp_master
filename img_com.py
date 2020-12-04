import os 
import sys 
from PIL import Image 
from easygui import *
  
# define a function for 
# compressing an image 
def compressMe(file, verbose = False,k=75): 
    
      # Get the path of the file 
    # filepath = os.path.join(os.getcwd(),  
    #                         file) 
      
    # open the image 
    picture = Image.open(file) 
    print(file)
    # Save the picture with desired quality 
    # To change the quality of image, 
    # set the quality variable at 
    # your desired level, The more  
    # the value of quality variable  
    # and lesser the compression 

    saved="./img_compressed"
    picture.save(saved,  
                 "JPEG",  
                 optimize = True,  
                 quality = k) 
    return saved
  
# Define a main function 
def main(): 
    
    verbose = False
      
    # checks for verbose flag 
    if (len(sys.argv)>1): 
        
        if (sys.argv[1].lower()=="-v"): 
            verbose = True       
    
    file = fileopenbox()
    text="Enter quality factor 10 - 100"
    title="Image compression"
    d_int = 75
    lower = 10
    upper=100

    output=integerbox(text,title,d_int,lower,upper)
    compressMe(file,verbose,output)
    
    print("Done") 
  
# # Driver code 
# if __name__ == "__main__": 
#     main() 