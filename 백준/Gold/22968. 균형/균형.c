#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {
	int s_of_n[44];
	s_of_n[1] = 1;
	s_of_n[2] = 2;
	for (int i = 3; i < 44; i++) {
		s_of_n[i] = s_of_n[i-1]+s_of_n[i-2]+1;
	}
	int t;
	scanf("%d", &t);
	int temp;
	for (int i = 0; i < t; i++) {
		scanf("%d", &temp);
		for (int j = 1; j <= 42; j++) {
			if (s_of_n[j] <= temp && temp < s_of_n[j+1]) {
				printf("%d\n", j);
				break;
			}
		}
	}
}
