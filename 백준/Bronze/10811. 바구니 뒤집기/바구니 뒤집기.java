import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

//        String input = "src/baekJoon/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] NM = br.readLine().split(" ");
//        System.out.println(Arrays.toString(NM));

        int N = Integer.parseInt(NM[0]);
        int M = Integer.parseInt(NM[1]);

        // 숫자 넣어주기
        int [] result = new int [N];

        for (int i = 0; i < N; i ++){
            result[i] = i + 1;
        }

        for (int i = 0; i < M; i++){
            String[] line = br.readLine().split(" ");
            int A = Integer.parseInt(line[0]) -1;
            int B = Integer.parseInt(line[1]) -1;

            while (A<B){
                int temp = result[A];
                result[A] = result[B];
                result[B] = temp;

                A++;
                B--;
            }
        }

        for (int i = 0; i < N; i++){
            System.out.print(result[i] + " ");
        }
    }
}
