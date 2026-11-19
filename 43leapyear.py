import calendar as c
y=int(input("Enter a year: "))
if c.isleap(y):
	print(y,"is leap year")
else:
	print(y,"is not leap year")
