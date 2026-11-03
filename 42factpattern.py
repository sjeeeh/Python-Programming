def fact(n):
	f=1
	for i in range(1,n+1):
		f*=i
	return f
n=int(input("No of terms?"))
sum=0
for i in range(1,n+1):
	sum=sum+(i**i)/fact(i)
print("Sum of the series:",sum)
