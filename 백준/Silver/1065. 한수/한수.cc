#include <iostream>

using namespace std;

bool isDeung(int n) {
	int gongcha = n % 10 - (n/10)%10;
	while (n >= 10) {
		if (gongcha == n % 10 - (n / 10) % 10) {
			n /= 10;
		}
		else return false;
	}
	return true;
}

int main() {
	int n;
	cin >> n;

	int cnt = 0;
	for (int i = 1; i <= n; i++) {
		if (i < 100) cnt++;
		else if (isDeung(i)) cnt++;
	}
	cout << cnt;
}