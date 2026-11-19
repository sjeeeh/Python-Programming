def is_armstrong(n):
	t=sum(int(d)**len(str(n)) for d in str(n))
	return t==n
