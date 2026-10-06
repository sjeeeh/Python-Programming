l1=list(map(int,input("Enter first list: ").split()))
l2=list(map(int,input("Enter second list: ").split()))
print("Same length : ",len(l1)==len(l2))
print("Same sum : ",sum(l1)==sum(l2))
if set(l1)&set(l2):
	print("Common value exist!")
else:
	print("No common value!")
