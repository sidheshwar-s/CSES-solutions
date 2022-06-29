#include <bits/stdc++.h>
using namespace std;

const int modulo = 1e9 + 7;

int main() {
	long long n;
	cin >> n;
	std::vector<long long > dp(n+1, 0);
	dp[0] = 1;
	for(int i = 1; i < n+1; i ++) {
		for(int j = 1; j < 7; j ++) {
			if(i - j >= 0) dp[i] = (dp[i] + dp[i - j]) % modulo;
		}
	}
	cout << dp[n] << "\n";
} 