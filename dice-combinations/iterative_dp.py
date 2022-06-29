num = int(input())
modulo = 10 ** 9 + 7
dp = [0] * (num + 1)
dp[0] = 1
for i in range(1, num+1):
	for j in range(1, 7):
		if i - j >= 0: dp[i] += dp[i - j]
print(dp[-1] % modulo)