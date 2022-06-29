import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

inf = 1e10
modulo = 1e9 + 7
n, target = map(int, input().split())
coins = list(map(int, input().split()))

dp = [[0] * (target+1) for _ in range(n+1)]
dp[0][0] = 1

for i in range(1, n+1):
	for j in range(target+1):
		if j - coins[i-1] >= 0:
			pick = dp[i][j - coins[i-1]]
			not_pick = dp[i-1][j]
			dp[i][j] = pick + not_pick
		else:
			not_pick = dp[i-1][j]
			dp[i][j] = not_pick

result = int(dp[n][target] % modulo)
print(result)
