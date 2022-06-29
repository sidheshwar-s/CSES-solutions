import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
num = int(input())
dp = [-1] * (num + 1)
modulo = 10 ** 9 + 7
sys.setrecursionlimit(10**6)
def find_ways(n):
	if dp[n] != -1: return dp[n]
	if n == 0: return 1
	ans = 0
	for i in range(1, 7):
		if n - i >= 0: ans += find_ways(n - i)
	dp[n] = ans
	return ans % modulo
ans = find_ways(num)
print(ans)