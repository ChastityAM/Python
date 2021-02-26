import os

print(os.getcwd())
#makes dir
os.mkdir("made_w_os")
print(os.listdir(os.getcwd()))
#deletes it
os.rmdir("made_w_os")

print(os.stat("lists.py"))