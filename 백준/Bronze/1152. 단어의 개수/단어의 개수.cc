#include <iostream>
#include <string>

using namespace std;

int main() {
	string str;
	getline(cin, str);

	int cnt = 0;
	for (int i = 0; i < str.length(); i++) {
		if (str == " ") {
			cout << 0;
			return 0;
		}
		if (i != 0 && str.at(i) == ' ' && i != str.length() - 1) cnt++;
	}

	cout << cnt + 1;
	return 0;
}