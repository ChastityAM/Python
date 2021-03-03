# Program to display the Fibonacci sequence up to 1000
def fib(n):
	N1=0
	N2=1
	previous_fib = N1
	current_fib = N2

	while current_fib < 1000:
		print(current_fib)
		temp = current_fib
		current_fib = current_fib + previous_fib
		previous_fib = temp
fib(1000)

