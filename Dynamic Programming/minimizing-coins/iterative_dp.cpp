#include <bits/stdc++.h>
using namespace std;

const long long inf = 1e10;

int main() {
	long long n, target;
	cin >> n >> target;
	long long coin;
	vector<long long> coins;
	for(int i = 0; i < n; i++) {
		cin >> coin;
		coins.push_back(coin);
	}
	vector<vector<long long >> dp(2, vector<long long>(target+1, inf));
	dp[0][0] = 0;
	int idx;
	for(long long i = 1; i < n+1; i++) {
		idx = i & 1;
		for(long long j = 0; j < target+1; j++) {
			long long pick = j - coins[i-1] >= 0 ? 1 + dp[idx][j - coins[i-1]] : inf;
			long long not_pick = dp[1 - idx][j];
			dp[idx][j] = min(pick, not_pick);
		}
	}
	long long ans = dp[idx][target];
	if(ans == inf) ans = -1;
	cout << ans << "\n";
} 