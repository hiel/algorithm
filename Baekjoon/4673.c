// https://www.acmicpc.net/problem/4673

#include <stdio.h>

int main () {
    int i, sum, ary[20000] = {0, };

    for (i = 1; i < 10001; i++) {
        sum = i + i % 10;

        if (i > 9) {
            sum += i / 10 % 10;

            if (i > 99) {
                sum += i / 100 % 10;

                if (i > 999) {
                    sum += i / 1000 % 10;

                    if (i > 9999) {
                        sum += i / 10000 % 10;
                    }
                }
            }
        }

        ary[sum-1] = 1;
    }

    for (i = 0; i < 10000; i++) {
        if (ary[i] == 0) {
            printf("%d\n", i+1);
        }
    }

    return 0;
}
