import os

print(os.getcwd())
#makes dir
#os.mkdir("./resources")
os.chdir("./resources")
print(os.getcwd())

print(os.listdir(os.getcwd()))
#deletes it
os.rmdir("made_w_os")

print(os.stat("lists.py"))

this_folder = os.getcwd()
print(this_folder)
data_folder = os.path.join(this_folder, "data", "votes.csv")
print(data_folder)
print(os.path.basename(data_folder))
print(os.path.dirname(data_folder))
