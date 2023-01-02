#include <iostream>

using namespace std;

int main() {
	int a, b, c;
	int cnt[10] = {0};
	cin >> a >> b >> c;
	int n = a * b * c;

	while (n > 0) {
		cnt[n % 10]++;
		n /= 10;
	}

	for (int i = 0; i < 10; i++) cout << cnt[i] << endl;
	return 0;
}