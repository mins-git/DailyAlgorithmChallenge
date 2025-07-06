import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {


        String input = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] NM = br.readLine().split(" ");
        int N = Integer.parseInt(NM[0]);
        int M = Integer.parseInt(NM[1]);

        int[] arrayN = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int[] prefixSum = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            prefixSum[i] = prefixSum[i - 1] + arrayN[i - 1];
        }

        StringBuilder sb = new StringBuilder();


        for (int t = 0; t < M; t++){

            String[] Q = br.readLine().split(" ");
            int A = Integer.parseInt(Q[0]);
            int B = Integer.parseInt(Q[1]);

            int answer = prefixSum[B] - prefixSum[A - 1];
            sb.append(answer).append("\n");

        }

        System.out.println(sb);


        /*
        수 N개 i부터 ~ j까지의 합을 구하는 프로그램 작성
         */
    }
}
