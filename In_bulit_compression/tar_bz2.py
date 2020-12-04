# Python program to demonstrate command line arguments
import sys
import tarfile
from tqdm import tqdm 
# total arguments
def compress(tar_file, members):
    """
    Adds files (`members`) to a tar_file and compress it
    """
    # open file for gzip compressed writing
    tar = tarfile.open(tar_file, mode="w:bz2")
    # with progress bar
    # set the progress bar
    progress = tqdm(members)
    for member in progress:
        # add file/folder/link to the tar file (compress)
        tar.add(member)
        # set the progress description of the progress bar
        progress.set_description(f"Compressing {member}")
    # close the file
    tar.close()

def decompress(tar_file, path, members=None):
    """
    Extracts `tar_file` and puts the `members` to `path`.
    If members is None, all members on `tar_file` will be extracted.
    """
    tar = tarfile.open(tar_file, mode="r:bz2")
    if members is None:
        members = tar.getmembers()
    # with progress bar
    # set the progress bar
    progress = tqdm(members)
    for member in progress:
        tar.extract(member, path=path)
        # set the progress description of the progress bar
        progress.set_description(f"Extracting {member.name}")
    # or use this
    # tar.extractall(members=members, path=path)
    # close the file
    tar.close()

   
def main() :
    n = len(sys.argv)
    print("Total arguments passed:", n)
    # Arguments passed
    print("\nName of Python script:", sys.argv[0]) 
    print("\nName of input text file:", sys.argv[1]) 
    print("\nArguments passed:", end = " ")
    for i in range(1, n):
        print(sys.argv[i], end = " ")
    print("\n")
    print("Compression of file :",sys.argv[1])
    compress("compressed.tar.bz2", [sys.argv[1]])
    decompress("compressed.tar.bz2", "extracted_bz2")
# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 

