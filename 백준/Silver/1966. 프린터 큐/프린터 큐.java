import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCase = Integer.parseInt(br.readLine());

        for (int t = 0; t < testCase; t++) {
            String[] input = br.readLine().split(" ");
            int n = Integer.parseInt(input[0]); // 문서 개수
            int m = Integer.parseInt(input[1]); // 궁금한 문서 위치

            String[] priorities = br.readLine().split(" ");
            Queue<int[]> queue = new LinkedList<>(); // [index, priority]

            for (int i = 0; i < n; i++) {
                queue.offer(new int[]{i, Integer.parseInt(priorities[i])});
            }

            int count = 0;
            while (!queue.isEmpty()) {
                int[] front = queue.poll();
                boolean hasHigher = false;

                for (int[] doc : queue) {
                    if (doc[1] > front[1]) {
                        hasHigher = true;
                        break;
                    }
                }

                if (hasHigher) {
                    queue.offer(front); // 중요도 높은게 있다면 다시 뒤로
                } else {
                    count++;
                    if (front[0] == m) {
                        System.out.println(count);
                        break;
                    }
                }
            }
        }
    }
}
