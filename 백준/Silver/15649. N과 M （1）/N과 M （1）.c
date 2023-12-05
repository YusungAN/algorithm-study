#include <stdio.h>
#include <string.h>

int arr[8];
int arr_idx = 0;
int n, m;

void bt(int idx) {
    if (idx == m) {
        for (int i = 0; i < arr_idx; i++) printf("%d ", arr[i]);
        printf("\n");
        return;
    }

    for (int i = 1; i <= n; i++) {
        int flag = 0;
        for (int j = 0; j < arr_idx; j++) {
            if (arr[j] == i) {
                flag = 1;
                break;;
            }
        }
        if (flag) continue;
        arr[arr_idx++] = i;
        bt(idx+1);
        arr_idx--;
    }
}

int main() {
    scanf("%d %d", &n, &m);
    bt(0);
}