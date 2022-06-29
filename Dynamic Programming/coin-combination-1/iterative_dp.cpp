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
	vector<int> dp(target+1, 0);
	dp[0] = 1;
	for(int i = 1; i < target+1; i++) {
		for(int coin: coins) {
			if((i - coin) >= 0) dp[i] = (dp[i] + dp[i - coin]) % modulo;
		}
	}
	cout << dp[target] << "\n";
} 