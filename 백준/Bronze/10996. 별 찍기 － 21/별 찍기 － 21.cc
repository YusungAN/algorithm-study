#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;

	for (int i = 0; i < n*2; i++) {
		if (i % 2 == 1) {
			for (int j = 0; j < n; j++) {
				if (j % 2 == 1) cout << '*';
				else cout << ' ';
			}
		}
		if (i % 2 == 0) {
			for (int j = 0; j < n; j++) {
				if (j % 2 == 0) cout << '*';
				else cout << ' ';
			}
		}
		cout << endl;
	}
	return 0;
}