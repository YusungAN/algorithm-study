#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int n, w[16][16], dp[1 << 16][16];
const int INF = 1000000000;


int _min(int a, int b) {
	return a > b ? b : a;
}

int tsp(int cur, int visited) {
	if (dp[visited][cur] != -1)
		return dp[visited][cur];
	if (visited == (1 << n) - 1) {
		if (w[cur][0] != 0)
			return w[cur][0];
		return INF;
	}

	dp[visited][cur] = INF;
	for (int i = 0; i < n; i++) {
		if (visited & (1 << i) || w[cur][i] == 0) continue;
		dp[visited][cur] = _min(dp[visited][cur], tsp(i, visited | (1 << i)) + w[cur][i]);
	}

	return dp[visited][cur];

}

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			scanf("%d", &w[i][j]);
		}
	}
	memset(dp, -1, sizeof(dp));
	printf("%d", tsp(0, 1));
}
