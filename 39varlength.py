def add(*args):
	"""This function accepts no.of arguments and return their sum"""
	sum=0
	for i in args:
		sum+=i
	return sum
print("Sum of 2,3,4: ",add(2,3,4))
print("Sum of 10,20,30,40: ",add(10,20,30,40))
print("Sum of 5,15: ",add(5,15))
print("\nDocstring")
print(add.__doc__)
