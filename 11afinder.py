names=list(input("Enter first names(, seperated):\n").split(','))
count=0
for i in names:
	count+=i.lower().count('a')
print("no.of 'a': ",count)
