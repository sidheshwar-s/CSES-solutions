import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

inf = 1e10
n, target = map(int, input().split())
coins = list(map(int, input().split()))
dp = [[-1] * (target+1) for _ in range(n+1)]

def solution(index, total):
	if index >= n:
		return inf
	if total == 0:
		return 0
	if total < 0:
		return inf
	if dp[index][total] != -1:  
		return dp[index][total]
	
	pick = 1 + solution(index, total - coins[index])
	not_pick = solution(index+1, total)
	dp[index][total] = min(pick, not_pick)
	return dp[index][total]

result = solution(0, target)
print(result if result != inf else -1)