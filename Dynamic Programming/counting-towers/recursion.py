import resource, sys
sys.setrecursionlimit(10000)
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))

inf = 1e10
modulo = 1e9 + 7

def solution():
    n = int(input())

    def recurse(index, prev_seperated):
        if index == 1:
            # placing two different tiles of width 1
            if not prev_seperated:
                return 1
            # placing single tile of width 2
            if prev_seperated:
                return 1
        elif prev_seperated:
            extend_both = recurse(index - 1, True)
            extend_one = 2 * recurse(index - 1, True)
            not_extend = recurse(index - 1, False) + recurse(index - 1, True)
            return extend_both + not_extend + extend_one
        else:
            extend_both = recurse(index - 1, False)
            place_new = recurse(index - 1, True) + recurse(index - 1, False)
            return extend_both + place_new

    return recurse(n, True) + recurse(n, False)

ans = solution()	
print(ans)
 
