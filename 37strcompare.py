def compare(s1,s2,n):
	return s1[:n]==s2[:n]
s1=input("Enter S1: ")
s2=input("Enter S2: ")
n=int(input("Enter n : "))
print(compare(s1,s2,n))
