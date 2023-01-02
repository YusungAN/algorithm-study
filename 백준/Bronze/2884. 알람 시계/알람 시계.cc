#include <iostream>

using namespace std;

int main() {
	int h, m;
	
	cin >> h >> m;
	if (h == 0) h = 24;
	
	if (m >= 45) {
		if (h == 24) h = 0;
		cout << h << ' ' << m - 45;
	}
	else cout << h - 1 << ' ' << 60 + (m - 45);
	return 0;
}