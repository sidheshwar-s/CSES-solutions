import resource, sys
sys.setrecursionlimit(10000)
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

inf = 1e10
modulo = 1e9 + 7

def solution():
    n, m = map(int, input().split())
    dp = [[0] * (m+1) for _ in range(n+1)] 
    for i in range(1, n+1):
        for j in range(1, m+1):
            # vertical cuts
            if i == j:
                dp[i][j] = 0
            else:
                vert = inf
                for y in range(1, j):
                    vert = min(vert, 1 + dp[i][j-y] + dp[i][y])

                # horizontal cuts
                hort = inf
                for x in range(1, i):
                    hort = min(hort, 1 + dp[i-x][j] + dp[x][j])
                dp[i][j] = min(vert, hort)

    return dp[n][m]


print(solution())
