#include <iostream>

using namespace std;

int main() {
	char *str = new char[101];
	int n[26];
	fill_n(n, 26, -1);
	cin >> str;
	for (int i = 0; str[i] != NULL; i++) {
		for (int j = 0; j < 26; j++) {
			if ((int)str[i] == 97 + j && n[j] == -1) n[j] = i;
		}
	}

	for (int i = 0; i < 26; i++) cout << n[i] << ' ';

}