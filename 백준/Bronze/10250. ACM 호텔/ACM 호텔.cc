#include <iostream>

using namespace std;

int main() {
	int T, temp;
	cin >> T;
	int **arr = new int*[T];
	for (int i = 0; i < T; i++) {
		arr[i] = new int[3];
		cin >> arr[i][0] >> arr[i][1] >> arr[i][2]; // 0 - H, 1 - W, 2 - N번재 손님
	}
	for (int i = 0; i < T; i++) {
		temp = (arr[i][2] % arr[i][0] == 0) ? arr[i][2] / arr[i][0] : arr[i][2] / arr[i][0] + 1;
		if (temp < 10) cout << ((arr[i][2] % arr[i][0] == 0) ? arr[i][0] : arr[i][2] % arr[i][0]) << 0 << temp << endl;
		else cout << ((arr[i][2] % arr[i][0] == 0) ? arr[i][0] : arr[i][2] % arr[i][0]) << temp << endl;
	}
	return 0;
}