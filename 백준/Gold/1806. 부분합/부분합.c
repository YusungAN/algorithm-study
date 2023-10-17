#include <stdio.h>

int arr[100000];

int max(int a, int b) {
    return a > b ? a : b;
}

int min(int a, int b) {
    return a < b ? a : b;
}

int main() {
    int n, S;
    scanf("%d %d", &n, &S);

    for (int i = 0; i < n; i++) scanf("%d", arr+i);

    int s = 0, e = 0, ans = n+1, now = arr[0];

    while (s <= e && e < n) {
        if (now >= S) {
            ans = min(ans, e-s+1);
            now -= arr[s++];
        } else {
            now += arr[++e];
        }
    }
    
    printf("%d\n", ans != n+1 ? ans : 0);
}