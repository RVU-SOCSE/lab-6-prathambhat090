
import os
import shutil
#copying a file
shutil.copy("myfile.txt", "myfile_copy.txt")
#changing directory
os.chdir("C:/Users/RVUW252/Desktop/prathampy")
print("Current Directory:", os.getcwd())
#making a new directory
os.mkdir("new_directory")
print("Directory 'new_directory' created.")
#rename a file
os.rename("myfile_copy.txt", "myfile_renamed.txt")
print("File renamed to 'myfile_renamed.txt'.")
#removing a file
os.remove("myfile_renamed.txt")
print("File 'myfile_renamed.txt' removed.")
#removing a directory
os.rmdir("new_directory")
print("Directory 'new_directory' removed.")
