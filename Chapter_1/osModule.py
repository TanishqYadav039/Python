# Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that.  

import os

path = os.getcwd()
print(os.listdir(path))