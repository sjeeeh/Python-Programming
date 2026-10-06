num=list(map(int,input("Enter values: ").split()))
for i in range(len(num)):
	if num[i]>100:
		num[i]='over'
print(num)
