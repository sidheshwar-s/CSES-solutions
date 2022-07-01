#include <bits/stdc++.h>
using namespace std;

const long long inf = 1e10;
const long long modulo = 1e9 + 7;

int main() {
	
	int maxn = 1e6 + 6;
	vector<vector<long long>> dp(maxn+1, vector<long long>(2, 0));
	dp[1][0] = dp[1][1] = 1;

	for(int i = 2; i < maxn; i++) {
		dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][0]) % modulo;
		dp[i][1] = (dp[i-1][1] + (2 * dp[i-1][1]) + dp[i-1][0] + dp[i-1][1]) % modulo;
		dp[i][0] %= modulo;
		dp[i][1] %= modulo;
	}

	int t, n; cin >> t;
	for(int j = 0; j < t; j++) {
		cin >> n;
		cout << (dp[n][0] + dp[n][1]) % modulo << "\n";
	}
} 