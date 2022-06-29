import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

inf = 1e10
n, target = map(int, input().split())
coins = list(map(int, input().split()))
dp = [[0] * (target+1) for _ in range(2)]

for i in range(n+1):
	idx = i & 1
	for j in range(target+1):
		if i == 0 and j > 0:
			dp[idx][j] = inf
			continue
		pick = 1 + dp[idx][j - coins[i-1]] if j - coins[i-1] >= 0 else inf
		not_pick = dp[1 - idx][j]
		dp[idx][j] = min(pick, not_pick)

result = dp[idx][target]
print(result if result != inf else -1)