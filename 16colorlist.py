l1=input("Enter colors in first list: ").split()
l2=input("Enter colors in second list: ").split()
for c in l1:
	if c not in l2:
		print(c)
