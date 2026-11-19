import Armstrong as arm
l=int(input("Enter lower limit:"))
u=int(input("Enter upper limit:"))
print("Armstrong numbers:")
for i in range(l,u+1):
	if arm.is_armstrong(i):
		print(i)
