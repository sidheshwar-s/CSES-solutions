#include <bits/stdc++.h>
using namespace std;

const long long inf = 1e10;
const long long modulo = 1e9 + 7;

int main() {
	long long n, target;
	cin >> n >> target;
	long long coin;
	vector<long long> coins;
	for(int i = 0; i < n; i++) {
		cin >> coin;
		coins.push_back(coin);
	}
	vector<vector<int>> dp(2, vector<int>(target+1, 0));
	dp[0][0] = 1;
	int idx;
	for(int i = 1; i < n+1; i++) {
		idx = i & 1;
		for(int j = 0; j < target+1; j ++) {
			if((j - coins[i-1]) >= 0) {
				int pick = dp[idx][j - coins[i-1]];
				int not_pick = dp[1 - idx][j];
				dp[idx][j] = pick + not_pick;
			} else {
				int not_pick = dp[1 - idx][j];
				dp[idx][j] = not_pick;
			}
			dp[idx][j] %= modulo;
		}
	}
	cout << dp[idx][target] << "\n";
} 