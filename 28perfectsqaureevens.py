ll=int(input("Enter lower limit: "))
ul=int(input("Enter upper limit: "))
for i in range(max(ll,1000),min(ul,9999)):
	if int(i**0.5)**2==i and all(int(d)%2==0 for d in str(i)):
		print(i)
