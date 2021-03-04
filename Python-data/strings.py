str1 = "Hello"
str2 = "World"

my_message = "I said 'Hello World'"
my_greeting = 'I will say "Hello World"'

length_of_string = len(str1)
print(length_of_string)

message = "hello world"
print(message.capitalize())
print(message.split(" "))
print(message.replace(" ", "@"))

#to print a string and an int, pass them as strings
x = 22
y = "The answer is "
print(y + str(x))

#you can parse a number string to an int, but it has to be a number
num = int("31")
print(num)


a = 42
b= "Her age is {}, {}"
message = " so cool!"
z = b.format(a, message)
print(z)

c = 33
d = "I ate"
message2 = "pizzas and nearly died!"
r = f"{d} {c} {message2}, {6 * 9}"
print(r)
