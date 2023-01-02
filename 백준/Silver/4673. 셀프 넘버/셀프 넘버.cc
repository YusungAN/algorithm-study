#include <iostream>

using namespace std;

int d(int n) {
	int res = n;
	while (n > 0) {
		res += n % 10;
		n /= 10;
	}
	return res;
}

int main() {
	bool b;

	for (int i = 1; i <= 10000; i++) {
		b = false;
		for (int j = 1; j <= i; j++) {
			if (d(j) == i) b = true;
		}
		if (!b) cout << i << endl;
	}
}