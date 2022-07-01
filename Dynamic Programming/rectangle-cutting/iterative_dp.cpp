#include <bits/stdc++.h>
using namespace std;

const long long inf = 1e10;
const long long modulo = 1e9 + 7;

int min(int a, int b) {
	if (a < b) return a;
	else return b;
}

int main() {
	int n, m; cin >> n >> m;
	vector<vector<long>> dp(n+1, vector<long>(m+1, 0));

	for(int i = 1; i < n+1; i++) {
		for(int j = 1; j < m+1; j++) {
			if(i == j) {
				dp[i][j] = 0;
			} else {
				// horizontal cut
				long hort = inf;
				for(int x = 1; x < i; x++) {
					hort = min(hort, 1 + dp[x][j] + dp[i-x][j]);
				}

				// vertical cur
				long vert = inf;
				for(int y = 1; y < j; y++) {
					vert = min(vert, 1 + dp[i][y] + dp[i][j-y]);
				}

				dp[i][j] = min(vert, hort);
			}
		}
	}

	cout << dp[n][m] << "\n";
} 