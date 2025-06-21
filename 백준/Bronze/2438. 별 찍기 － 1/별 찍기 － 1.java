import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

//        String input = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int starCnt = Integer.parseInt(br.readLine());

        for (int i = 1; i <= starCnt; i++){

            for (int j = 0; j< i; j++){
                System.out.print("*");
            }
            System.out.println();
        }

        // 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
    }
}
