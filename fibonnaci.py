# Program to display the Fibonacci sequence up to 1000


from functools import lru_cache 
 
@lru_cache(maxsize = 1000) 
def fibonacci(n): 
	if n==1: 
		return 1 
	if n==2: 
		return 1 
	elif n>2: 
		return fibonacci(n-1) + fibonacci(n-2) 
 
for i in range(1,1001): 
	print(i,':',fibonacci(i))