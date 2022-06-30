import resource, sys
sys.setrecursionlimit(10000)
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

inf = 1e10
modulo = 1e9 + 7

def solution():
	n, max_price = map(int, input().split())
	book_price = list(map(int, input().split()))
	book_pages = list(map(int, input().split()))

	dp = [[-1] * (max_price + 1) for _ in range(n + 1)]

	def recurse(index, money_left):
		if index == 0:
			return 0 if money_left >= 0 else -inf
		if money_left <= 0:
			return -inf
		if dp[index][money_left] != -1:
			return dp[index][money_left]
		pick = book_pages[index-1] + recurse(index-1, money_left - book_price[index-1])
		not_pick = recurse(index-1, money_left)
		dp[index][money_left] = max(pick, not_pick)
		return dp[index][money_left]

	return recurse(n, max_price)

ans = solution()	
print(ans)
