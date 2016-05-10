A, N, K = map(int, input().split())
for i in range(K):
	print(A%(N+1), end=' ')
	A = A//(N+1)
print('')