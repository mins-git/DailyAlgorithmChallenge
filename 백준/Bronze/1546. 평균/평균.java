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

        int N = Integer.parseInt(br.readLine());
        int[] realScore = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        double max = Arrays.stream(realScore).max().getAsInt();
        double result = 0;

        for (int i = 0; i < N; i++){
            result += (realScore[i] / max) * 100;
        }

        System.out.println(result / N);


        /*

        점수를 조작하려고함.
        자기 점수 중 최댓값 = M
        모든 점수를 점수/M*100 함.


         */


    }
}
