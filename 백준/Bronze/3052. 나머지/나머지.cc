#include <iostream>

using namespace std;

int main() {
	int in[10];
	int n[42] = { 0 };

	for (int i = 0; i < 10; i++) {
		cin >> in[i];
		n[in[i] % 42]++;
	}

	int cnt = 0;
	for (int i = 0; i < 42; i++) {
		if (n[i] != 0) cnt++;
	}
	cout << cnt;


}