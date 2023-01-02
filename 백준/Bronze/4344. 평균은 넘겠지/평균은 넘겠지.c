#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
int main(void) {
	int num;
	int student[100];
	int score[1000];
	int sum = 0;
	float ave = 0;
	int cnt=0;
	float p[1000];
	scanf("%d", &num);

	for (int i = 0; i < num; i++) {
		ave = 0;
		cnt = 0;
		sum = 0;
		scanf("%d", &student[i]);
		for (int j = 0; j < student[i]; j++) {
			scanf("%d", &score[j]);
			sum += score[j];
		}
		ave = (float)sum / student[i];
		for (int j = 0; j < student[i]; j++) {
			if (ave < score[j]) cnt++;
		}
		p[i] = (float)cnt / student[i];
	}

	for (int i = 0; i < num; i++) {
		printf("%.3f%%\n", p[i] * 100);
	}
}