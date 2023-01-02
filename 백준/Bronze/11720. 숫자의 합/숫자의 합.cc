#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	char *str = new char[n+1];
	cin >> str;

	int sum = 0;
	for (int i = 0; i < n; i++) {
		sum += str[i] - '0';
	}

	cout << sum;
}