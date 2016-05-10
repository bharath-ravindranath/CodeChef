computed = {}
def increase(N):
	if(N in computed):
		return computed[N]
	a, b, c = N//2, N//3, N//4
	if( (a+b+c) > N):
		retValue = increase(a)+increase(b)+increase(c)
	else:
		retValue = N
	computed[N] = retValue
	return retValue


L = []
while True:
	try:
		L.append(int(input()))
	except EOFError:
		break
for N in L:
	N = increase(N)
	print(N)