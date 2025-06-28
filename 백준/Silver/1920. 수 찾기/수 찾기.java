import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {

        String input = "src/input.txt";
//      BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        int[] arrN = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        Arrays.sort(arrN);

        int M = Integer.parseInt(br.readLine());

        int[] arrM = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        for (int target : arrM){
            if (Arrays.binarySearch(arrN, target) >= 0){
                sb.append(1).append('\n');
            } else {
                sb.append(0).append('\n');
            }

        }
        
        System.out.print(sb);

        /*
        N개의 정수 있을때 이 안에 x라는 정수가 존재하는지 알아내는 프로그램 작성

        존재하면 1 존재하지 않으면 0
         */

    }
}
