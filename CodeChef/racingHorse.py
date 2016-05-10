T = int(input())
for j in range(T):
	N = int(input())
	S = list(map(int, input().split()))
	S.sort()
	dif = 999999999
	for i in range(0,len(S) - 2):
		if  ( dif > abs(S[i] - S[i + 1])):
			dif = abs(S[i] - S[i + 1])
	print(dif)