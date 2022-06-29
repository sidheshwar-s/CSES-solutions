import resource, sys
sys.setrecursionlimit(10000)
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

inf = 1e10
modulo = 1e9 + 7

n = int(input())

dp = [-1] * (n+1)

def solution(n):
	if n == 0:
		return 0
	if n <= 0:
		return inf
	if dp[n] != -1:
		return dp[n]
	# extracting every digit
	cur_num = n
	ans = inf
	while cur_num:
		digit = cur_num % 10
		if digit != 0: 
			ans = min(ans, 1 + solution(n - digit))
		cur_num //= 10
	dp[n] = ans
	return ans

ans = solution(n)	
print(ans)
