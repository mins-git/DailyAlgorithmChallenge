import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        String input = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        String[] inputStr = br.readLine().split(" ");
        int N = Integer.parseInt(inputStr[0]);
        int K = Integer.parseInt(inputStr[1]);

        if ( K > N - K){
            K = N - K;
        }

        int result = 1;

        for (int i = 0; i < K; i++){
            result *= (N - i);
            result /= (i + 1);
        }

        System.out.println(result);


        /*
        자연수 N과 K가 주어지면, 이항 계수 를 구하는 프로그램 작성.
        n! / r! * (n-r)!
         */
    }
}
