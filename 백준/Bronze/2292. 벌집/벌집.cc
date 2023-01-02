#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	int s = 2, i = 1, cnt = 1;
	while (true) {
		if (i <= n && n < s) {
			break;
		}
		i = s;
		s += 6 * cnt;
		cnt++;
	}

	cout << cnt;
	return 0;
}