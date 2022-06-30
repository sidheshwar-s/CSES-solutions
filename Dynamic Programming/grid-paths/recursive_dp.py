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

	dp = [[-1] * (n) for _ in range(n)]
	
	def recurse(x, y):
		if not (0 <= x < n and 0 <= y < n):
			return  0
		if dp[x][y] != -1:
			return dp[x][y]
		if matrix[x][y] == "*":
			return 0
		if x == n-1 and y == n-1:
			return 1
		right = recurse(x, y+1)
		down = recurse(x+1, y)
		dp[x][y] = right + down
		return dp[x][y]

	return recurse(0, 0)

ans = solution(n)	
print(ans)
