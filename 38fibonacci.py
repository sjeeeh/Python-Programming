def fib(n):
	return n if n<=1 else fib(n-1)+fib(n-2)
for i in range(int(input("How many tersm? "))):
	print(fib(i),end=" ")
