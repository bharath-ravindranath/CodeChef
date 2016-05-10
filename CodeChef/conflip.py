for j in range(int(input())):
	G = int(input())
	for i in range(G):
		I, N, Q = map(int, input().split())
		if( (N % 2 == 0) or Q == I ):
			print(N//2)
		else:
			print(N//2 + 1)
