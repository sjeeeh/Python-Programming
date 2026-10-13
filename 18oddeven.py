nums=map(int,input("Enter the list: ").split())
odd=[]
for i in nums:
	if i%2!=0:
		odd.append(i)
print(odd)
