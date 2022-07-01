import resource, sys
sys.setrecursionlimit(10000)
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

inf = 1e10
modulo = 1e9 + 7

def solution():
    s1 = input()
    s2 = input()
    n, m = len(s1), len(s2)
    result = lcs(s1, s2)
    return result


def lcs(s1, s2):
    n, m = len(s1), len(s2)
    dp = [[-1] * (m+1) for _ in range(n+1)]

    def recurse(i, j):
        if i == 0 or j == 0:
            return i or j
        elif dp[i][j] != -1:
            return dp[i][j]
        elif s1[i-1] == s2[j-1]:
            return recurse(i-1, j-1)
        else:
            return 1 + min(recurse(i-1, j), recurse(i, j-1), recurse(i-1, j-1))

    return recurse(n, m)

print(solution())
