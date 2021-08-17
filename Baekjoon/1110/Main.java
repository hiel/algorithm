// https://www.acmicpc.net/problem/1110

import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int a = n % 10;
        int b = (n / 10 + n % 10) % 10;
        int r = a * 10 + b;
        int count = 1;

        for (;;) {
            if (n == r) {
                System.out.println(count);
                System.exit(0);
            }

            a = r % 10;
            b = (r / 10 + r % 10) % 10;
            r = a * 10 + b;
            count++;
        }
    }
}
