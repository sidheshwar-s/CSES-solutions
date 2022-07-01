import resource, sys
sys.setrecursionlimit(10000)
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

inf = 1e10
modulo = 1e9 + 7

def solution():
    n = int(input())

    dp = [[-1] * (2) for _ in range(n+1)]

    def recurse(index, prev_seperated):
        if index == 1:
            # placing two different tiles of width 1    
            if not prev_seperated:
                return 1
            # placing single tile of width 2
            if prev_seperated:
                return 1
        if dp[index][prev_seperated] != -1:
            return dp[index][prev_seperated]
        elif prev_seperated:
            extend_both = recurse(index - 1, 1)
            extend_one = 2 * recurse(index - 1, 1)
            not_extend = recurse(index - 1, 0) + recurse(index - 1, 1)
            dp[index][prev_seperated] = (extend_both + not_extend + extend_one) % modulo
        else:
            extend_both = recurse(index - 1, 0)
            place_new = recurse(index - 1, 1) + recurse(index - 1, 0)
            dp[index][prev_seperated] = (extend_both + place_new) % modulo
        return dp[index][prev_seperated]    

    return (recurse(n, 1) + recurse(n, 0)) % modulo

t = int(input())
for _ in range(t):
    ans = solution()    
    print(int(ans))
 
