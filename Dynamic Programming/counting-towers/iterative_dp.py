import resource, sys
sys.setrecursionlimit(10000)
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

inf = 1e10
modulo = 1e9 + 7
maxn = int(1e6 + 6);


dp = [[0] * (2) for _ in range(maxn+1)]
dp[1][0] = 1
dp[1][1] = 1

for i in range(2, maxn+1):
    dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][0]) % modulo
    dp[i][1] = (dp[i-1][1] + (2 * dp[i-1][1]) + dp[i-1][0] + dp[i-1][1]) % modulo


t = int(input())
for _ in range(t):
    n = int(input())
    ans = (dp[n][0] + dp[n][1]) % modulo 
    print(int(ans))
 
