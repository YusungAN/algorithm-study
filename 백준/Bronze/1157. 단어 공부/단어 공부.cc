#include <iostream>
#include <string>

using namespace std;

int main() {
	
	string str;
	int cnt[26] = { 0 };
	cin >> str;
	
	for (int i = 0; i < str.length(); i++) {
		if ((int)(str.at(i)) >= 97) {
			cnt[(int)(str.at(i))-97]++;
		}
		else {
			cnt[(int)(str.at(i)) - 65]++;
		}
	}
	
	int imax = 0;
	for (int i = 0; i < 26; i++) {
		if (cnt[i] > cnt[imax]) {
			imax = i;
		}
	}
	
	bool aa = false;
	for (int i = 0; i < 26; i++) {
		if (aa && cnt[imax] == cnt[i]) {
			cout << '?';
			return 0;
		}
		else if (cnt[imax] == cnt[i]) aa = true;
	}

	cout << (char)(imax + 65);


	return 0;
}