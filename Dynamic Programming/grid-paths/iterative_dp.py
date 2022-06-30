import resource, sys
sys.setrecursionlimit(10000)
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

inf = 1e10
modulo = 1e9 + 7

n = int(input())

def solution(n):
	matrix = []
	for _ in range(n):
		matrix.append(list(input()))

	if matrix[0][0] == "*":
		return 0

	dp = [[0] * (n) for _ in range(n)]
	dp[0][0] = 1

	for i in range(n):
		for j in range(n):
			if matrix[i][j] != "*":
				if i-1 >= 0:
					dp[i][j] = (dp[i][j] + dp[i-1][j]) % modulo
				if j-1 >= 0:
					dp[i][j] = (dp[i][j] + dp[i][j-1]) % modulo	
	return int(dp[n-1][n-1])

ans = solution(n)	
print(ans)
