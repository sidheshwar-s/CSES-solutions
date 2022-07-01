#include <bits/stdc++.h>
using namespace std;

const long long inf = 1e10;
const long long modulo = 1e9 + 7;

int min(int a, int b) {
	if (a < b) return a;
	else return b;
}

int main() {
	string s1, s2; cin >> s1; cin >> s2;
	int n = s1.size(), m = s2.size(), idx;
	vector<vector<int>> dp(2, vector(m+1, 0));

	for(int i = 0; i < m+1; i++) {
		dp[0][i] = i;
	}
	dp[1][0] = 1;
	dp[0][0] = 0;

	for(int i = 1; i < n+1; i++) {
		idx = i & 1;
		dp[idx][0] = i;
		for(int j = 1; j < m+1; j++) {
			if(s1[i-1] == s2[j-1]) {
				dp[idx][j] = dp[1-idx][j-1];
			} else {
				dp[idx][j] = 1 + min(dp[1-idx][j], min(dp[idx][j-1], dp[1-idx][j-1]));
			}
		}
	}
	cout << dp[idx][m];
} 