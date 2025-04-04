import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        if (n == 0) {
            System.out.println(0);
            return;
        }

        List<Integer> opinion = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            opinion.add(Integer.parseInt(br.readLine()));
        }

        Collections.sort(opinion);

        int cut = (int) Math.round(n * 0.15);

        int sum = 0;
        for (int i = cut; i < n - cut; i++) {
            sum += opinion.get(i);
        }

        int average = (int) Math.round((double) sum / (n - cut * 2));
        System.out.println(average);
    }
}
