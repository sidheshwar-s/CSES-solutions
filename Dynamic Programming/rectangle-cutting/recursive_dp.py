import resource, sys
sys.setrecursionlimit(10000)
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

inf = 1e10
modulo = 1e9 + 7

def solution():
    n, m = map(int, input().split())
    dp = [[-1] * (m+1) for _ in range(n+1)] 

    def recurse(x, y):
        if x == y:
            return 0
        if x < 0 or y < 0:
            return 0
        if dp[x][y] != -1:
            return dp[x][y]
        # vertical cuts
        vert = inf
        for i in range(1, y):
            vert = min(vert, 1 + recurse(x, y-i) + recurse(x, i))

        # horizontal curs
        hort = inf
        for j in range(1, x):
            hort = min(hort, 1 + recurse(x-j, y) + recurse(j , y))

        dp[x][y] = min(vert, hort)
        return dp[x][y]

    return recurse(n, m)

print(solution())
