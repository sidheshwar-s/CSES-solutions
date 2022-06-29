import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

inf = 1e10
n, target = map(int, input().split())
coins = list(map(int, input().split()))

dp = [0] * (target+1) 
dp[0] = 1

for i in range(target+1):
	for coin in coins:
		if(i - coin >= 0):
			pick = dp[i - coin]
			dp[i] += pick 
print(dp[target])
