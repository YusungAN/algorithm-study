#include <iostream>
#include <string>

using namespace std;

int main() {
	int a, b;
	int aa[3], bb[3];
	cin >> a >> b;

	for (int i = 0; i < 3; i++) {
		aa[i] = a % 10;
		bb[i] = b % 10;
		a /= 10;
		b /= 10;
	}

	a = aa[0] * 100 + aa[1] * 10 + aa[2];
	b = bb[0] * 100 + bb[1] * 10 + bb[2];

	if (a > b) cout << a;
	else cout << b;

	return 0;
}