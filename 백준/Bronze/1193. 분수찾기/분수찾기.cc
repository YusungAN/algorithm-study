#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	int mom = 1, son = 1;
	int jogun = 1;
	int i = 0;
	while (true) {
		for (int j = 1; j <= jogun; j++) {
			if (jogun % 2 == 1) {
				mom = j;
				son = jogun + 1 - mom;
				i++;
				if (i == n) {
					std::cout << son << '/' << mom;
					return 0;
				}
			}
			else {
				son = j;
				mom = jogun + 1 - son;
				i++;
				if (i == n) {
					std::cout << son << '/' << mom;
					return 0;
				};
			}
		}
		jogun++;
	}

	return 0;
}