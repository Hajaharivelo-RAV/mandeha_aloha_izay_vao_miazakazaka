## write an existing file
## using the open() function and the write() function
## using the "a" mode for append, basically we add some text in the end of our document 
## or using the "w" mode for write, this one will re-write everything in our document
f = open("demofile.txt", "a")
f.write(" this is some new content I guess!")
f.close()
# now let's see the new content
s = open("demofile.txt", "r")
print(s.read())

# now the write mode now
f2 = open("demofile.txt", "w")
f2.write("Sh**t, I deleted the content, well it doesn't matter anyway")
f2.close()
s2 = open("demofile.txt", "r")
print(s2.read())

# let's creat a new file now with the "x" mode
n = open("new_file2.txt", "x")
n.write("Hello! this is a new file, still none of the things here matter!")
n.close()

s3 = open("new_file2.txt", "r")
print(s3.read())

## remove file with os module
import os

os.remove("demofile.txt")

# check if file exist

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

# delete folder with os.rmdir()
if os.path.exists("dir_2_rmv"):
  os.rmdir("dir_2_rmv")
else:
  print("The directory does not exist")
