# Python program to demonstrate command line arguments
import sys,os
import tarfile
from tqdm import tqdm #pip3 install tqdm
# total arguments
def compressor(tar_file, comp_mode):
    """
    Adds files (`members`) to a tar_file and compress it
    """
    # open file for gzip compressed writing
    tar = tarfile.open(tar_file, mode="w:"+comp_mode)
    # with progress bar
    # set the progress bar
    for member in os.listdir('./archive/'):
        # add file/folder/link to the tar file (compress)
        tar.add('./archive/'+member,member)
        # set the progress description of the progress bar
    # close the file
    tar.close()
    return tar_file

def decompressor(tar_file, out_path, tar_mode):
    """
    Extracts `tar_file` and puts the `members` to `path`.
    If members is None, all members on `tar_file` will be extracted.
    """
    tar = tarfile.open(tar_file, mode="r:"+tar_mode)
    # with progress bar
    # set the progress bar
    for member in tar.getmembers():
        tar.extract(member, path=out_path)
        # set the progress description of the progress bar
    # or use this
    # tar.extractall(members=members, path=path)
    # close the file
    tar.close()
    return out_path