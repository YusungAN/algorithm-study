#include <iostream>

using namespace std;

int main() {
	int a, b, v;
	cin >> a >> b >> v;
	int d1 = ((v - a) % (a - b) == 0) ? (v - a) / (a - b) : (v - a) / (a - b) + 1;
	cout << d1+1;

	return 0;
}