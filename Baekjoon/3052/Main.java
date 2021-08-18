// https://www.acmicpc.net/problem/3052

import java.util.HashMap;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main (String[] args) throws IOException {
        HashMap<Integer, Boolean> m = new HashMap<>();

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int i=0; i<10; i++) {
            m.put(Integer.parseInt(br.readLine()) % 42, true);
        }

        System.out.println(m.size());
    }
}
