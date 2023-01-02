#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int in_idx[100001];
int post[100001];
int in[100001];

void pre(int post_start, int post_end, int in_start, int in_end) {
	if (post_start > post_end) return;
	if (in_start > in_end) return;

	int root_idx = in_idx[post[post_end]];
	//printf("%d %d\n", root_idx, post[post_end]);
	printf("%d ", post[post_end]);
	pre(post_start, post_start+(root_idx-in_start)-1, in_start, root_idx - 1);
	pre(post_start + (root_idx - in_start), post_end-1, root_idx + 1, in_end);
}

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", in + i);
		in_idx[in[i]] = i;
	}
	for (int i = 0; i < n; i++) {
		scanf("%d", post + i);
	}
	pre(0, n - 1, 0, n - 1);
}
