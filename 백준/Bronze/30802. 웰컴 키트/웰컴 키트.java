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
        int[] teeSize = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int[] tp = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
        int T = tp[0];
        int P = tp[1];

        int resultT = 0;

        // teesize가 부족해서는 안되는상황이니, T로 6번 순회하면서
        // T/teesize 몫이 + 1 만큼 하면됨.

        for (int i = 0; i < 6; i++){
            int quotient = teeSize[i] / T;
            int remainder = teeSize[i] % T;

            if (remainder != 0){
                resultT += quotient + 1;
            } else{
                resultT += quotient;
            }

        }
        System.out.println(resultT);


        int resultP = N / P;
        int resultP1 = N % P;

        System.out.println(resultP + " " + resultP1);




        /*
        티셔츠 한장, 펜 한자루 제공하려고함.

        티셔츠는 동일 사이즈 T장 묶음으로만 주문 가능
        펜은 한종류로 P 자루씩 묶음 주문 OR 한자루씩 주문 가능.

        티셔츠 남아도 됨. 부족 X
        펜 남거나 부족하면 안되고 정확히 제공되어야함.

        티셔츠를 T장씩 최소 몇묶음 주문 해야될까? 그리고 펜 P자루씩 최대 몇묶음 주문 AND 한자루씩 몇개 주문?

        입력:
        첫줄 참가자수 N
        사이즈별 티셔츠 신청자수 공백으로 제공됨.
        T, P 순서로 입력됨.

        출력:
        티셔츠 T장씩 최소 몇묶음 주문?
        펜 P 자루씩 최대 몇묶음 주문 and 한자루씩 몇개?
         */
    }
}
