#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		for (int j = i; j < n-1; j++) {
			cout << ' ';
		}
		for (int j = i; j >= 0; j--) {
			cout << '*';
		}
		cout << endl;
	}
	return 0;
}