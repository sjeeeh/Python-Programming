s=input("Enter a sentence: ")
words=set(s.split())
count={}
for i in words:
	count[i]=s.count(i)
print(count)
