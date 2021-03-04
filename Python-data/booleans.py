

print(bool(42))
print(bool(["hello"]))
print(bool("Hello"))
print(bool(0))
print(bool([]))
print(bool("")) 
print(bool(None))
x = "Hello World"
y = ""
if (bool(x)):
    print(x)

if (bool(y)):
    print(y)   #Skipped because no content is in y