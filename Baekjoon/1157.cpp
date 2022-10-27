// https://www.acmicpc.net/problem/1157

#include <iostream>
using namespace std;

int main() {
    bool q = false;
    int i, t, r, m = 0, c[26] = {0, };
    char *s = new char[1000000];

    cin >> s;

    for (i=0; i<1000000; i++) {
        if (s[i] == '\0') {
            break;
        }

        t = int(s[i]) - 65;

        if (t > 25) {
            t -= 32;
        }

        c[t]++;
    }

    for (i=0; i<26; i++) {
        if (c[i] > m) {
            m = c[i];
            r = i;
            q = false;
        } else if (c[i] == m) {
            q = true;
        }
    }

    if (q == true) {
        cout << "?" << endl;
    } else {
        cout << char(r+65) << endl;
    }

    return 0;
}
