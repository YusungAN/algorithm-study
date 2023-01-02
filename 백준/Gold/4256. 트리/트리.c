#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <memory.h>

int in_idx[10001];
int pre[1001];
int in[1001];

void post(int pre_start, int pre_end, int in_start, int in_end) {
	if (pre_start > pre_end) return;
	if (in_start > in_end) return;

	int root_idx = in_idx[pre[pre_start]] - 1;

	post(pre_start + 1, pre_start + (root_idx - in_start), in_start, root_idx - 1);
	post(pre_start + (root_idx - in_start) + 1, pre_end, root_idx + 1, in_end);
	printf("%d ", pre[pre_start]);

}

int main() {
	int n;
	int k;
	scanf("%d", &k);

	for (int j = 0; j < k; j++) {
		memset(in_idx, 0, sizeof(in_idx));
		memset(pre, 0, sizeof(pre));
		memset(in, 0, sizeof(in));
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", pre + i);
		}
		for (int i = 0; i < n; i++) {
			scanf("%d", in + i);
			in_idx[in[i]] = i + 1;
		}
		post(0, n - 1, 0, n - 1);
		printf("\n");
	}
}
