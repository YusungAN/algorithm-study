#include <iostream>
#include <string>

using namespace std;

bool first(char c, char (&check)[100]) {
	for (int i = 0; check[i] != 0; i++) {
		if (check[i] == c) return false;
	}
	return true;
}

int main() {
	int n;
	cin >> n;
	string *str = new string[n];

	for (int i = 0; i < n; i++) {
		cin >> str[i];
	}

	char check[100] = { 0 };
	int cnt = 0;
	bool is = true;
	for (int i = 0; i < n; i++) {
		is = true;
		for (int i = 0; i < 100; i++) {
			check[i] = 0;
		}
		for (int j = 0; j < str[i].length(); j++) {
			if (j != 0 && str[i].at(j - 1) != str[i].at(j) && !first(str[i].at(j), check)) {
				is = false;
				break;
			}
			else {
				check[j] = str[i].at(j);
			}
		}
		if (is) cnt++;
	}

	cout << cnt;
	return 0;
}