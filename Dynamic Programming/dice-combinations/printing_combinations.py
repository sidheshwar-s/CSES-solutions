import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)

num = int(input())
result = []

def find_ways(n, cur_comb):
	if n == 0:
		result.append(cur_comb[:])
	for i in range(1, 7):
		if n - i >= 0:
			find_ways(n - i, cur_comb + [i])
find_ways(num, [])
print(result)