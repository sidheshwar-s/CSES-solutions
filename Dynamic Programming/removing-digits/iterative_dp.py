import resource, sys
sys.setrecursionlimit(10000)
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

inf = 1e10
modulo = 1e9 + 7

n = int(input())

def solution(n):
	if n < 10:
		return 1
	dp = [inf] * (n+1)
	dp[0] = 0

	for i in range(0, n+1):
		cur_num = i
		while cur_num:
			digit = cur_num % 10
			if digit != 0:
				dp[i] = min(dp[i], dp[i - digit] + 1)
			cur_num //= 10
	return dp[n]

ans = solution(n)	
print(ans)
