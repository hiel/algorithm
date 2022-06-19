// https://www.acmicpc.net/problem/10989

#include <stdio.h>

int main () {
    int n, t, a[10001] = {0, };

    scanf("%d", &n);

    while (n-- > 0) {
        scanf("%d", &t);
        a[t]++;
    }

    while (n++ < 10000) {
        if (a[n] > 0) {
            t = a[n];
            while (t-- > 0) {
                printf("%d\n", n);
            }
        }
    }

    return 0;
}
