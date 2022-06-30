import resource, sys
sys.setrecursionlimit(10000)
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

inf = 1e10
modulo = 1e9 + 7

def solution():
	n, max_price = map(int, input().split())
	book_price = list(map(int, input().split()))
	book_pages = list(map(int, input().split()))

	dp = [[0] * (max_price + 1) for _ in range(2)]

	for i in range(1, n+1):
		idx = i & 1
		for j in range(1, max_price+1):
			pick = book_pages[i-1] + dp[1 - idx][j - book_price[i-1]] if j >= book_price[i-1] else -inf
			not_pick = dp[1 - idx][j]
			dp[idx][j] = max(pick, not_pick)

	return dp[idx][max_price]

ans = solution()	
print(ans)
