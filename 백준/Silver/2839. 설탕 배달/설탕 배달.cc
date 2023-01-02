#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;

	int five = 0, three = 0;
	int ori = n;

	while (n - 5 >= 0) {
		n -= 5;
		five++;
	}

	while (n - 3 >= 0) {
		n -= 3;
		three++;
	}
	if (n != 0) {
		while (true) {
			five--;
			n += 5;
			if (n > ori) {
				cout << -1;
				return 0;
			}
			if (n % 3 == 0) {
				three += n / 3;
				break;
			}
		}
	}

	cout << five + three;
	return 0;
}