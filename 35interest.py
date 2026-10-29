def intrest(p,t,r):
	return p*r*t/100
p=float(input("Principal amount: "))
t=float(input("Time (in years) :  "))
rate_group=input("Customer senior citizen? (yes/no): ").strip().lower()
r=12 if rate_group in ["yes","y"] else 10
print("Simple interest: ",intrest(p,t,r))
