#include <bits/stdc++.h>
using namespace std;

const long long inf = 1e10;
const long long modulo = 1e9 + 7;

int solution(vector<int> &book_prices, vector<int> &book_pages, int n, int max_price) {
		vector<vector<int>> dp(2, vector<int>(max_price+1, 0));
		int idx;
		for(int i = 1; i <= n; i++) {
			idx = i & 1;
			for(int j = 1; j <= max_price; j++) {
				int pick = book_prices[i-1] <= j ? book_pages[i-1] + dp[1 - idx][j - book_prices[i-1]] : -inf;
				int not_pick = dp[1 - idx][j];
				dp[idx][j] = max(pick, not_pick);
			}
		}
		return dp[idx][max_price];
}

int main() {
	int n, max_price;
	cin >> n >> max_price;
	vector<int> book_prices(n), book_pages(n);
	for(int i = 0; i < n; i++) cin >> book_prices[i];
	for(int i = 0; i < n; i++) cin >> book_pages[i];

	cout << solution(book_prices, book_pages, n, max_price) << "\n";
} 