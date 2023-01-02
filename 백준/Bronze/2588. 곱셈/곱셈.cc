#include <iostream>

using namespace std;

int main() {
	int a, b, bb;
	int n[3] = { 0 };

	cin >> a >> b;
	bb = b;
	for (int i = 0; i < 3; i++) {
		n[i] = bb % 10;
		bb /= 10;
	}

	cout << a * n[0] << endl;
	cout << a * n[1] << endl;
	cout << a * n[2] << endl;
	cout << a * b << endl;
	
	return 0;
}