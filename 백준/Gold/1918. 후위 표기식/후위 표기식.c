#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

char stack[101];
int top = -1;

void push(char v) {
	if (top < 999) {
		stack[++top] = v;
	}
	else {
		printf("push fail");
	}
}

char pop() {
	if (top > -1) {
		return stack[top--];
	}
	else {
		return 0;
	}
}

int main() {
	char s[101];
	scanf("%s", s);

	for (int i = 0; s[i] != NULL; i++) {
		if (65 <= s[i] && s[i] <= 90) {
			printf("%c", s[i]);
		}
		else {
			if (s[i] == '(') {
				push(s[i]);
			}
			else if (s[i] == '*' || s[i] == '/') {
				if (stack[top] == '*' || stack[top] == '/') {
					printf("%c", pop());
				}
				push(s[i]);
			}
			else if (s[i] == '+' || s[i] == '-') {
				while (top > -1 && stack[top] != '(') {
					printf("%c", pop());
				}
				push(s[i]);
			}
			else {
				while (stack[top] != '(') {
					printf("%c", pop());
				}
				pop();
			}
		}
	}
	while (top > -1) {
		printf("%c", pop());
	}
}
