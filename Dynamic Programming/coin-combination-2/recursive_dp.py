import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

inf = 1e10
n, target = map(int, input().split())
coins = list(map(int, input().split()))

dp = [[-1] * (target+1) for _ in range(n+1)]

def solution(index, total):
	if total == 0 or index == 0:
		return 1 if total == 0 else 0
	if dp[index][total] != -1:
		return dp[index][total]
	elif coins[index-1] <= total:
		pick = solution(index, total - coins[index-1])
		not_pick = solution(index-1, total)
		dp[index][total] = pick + not_pick
	else:
		not_pick = solution(index-1, total)
		dp[index][total] = not_pick
	return dp[index][total]

result = solution(n, target)
print(result)
