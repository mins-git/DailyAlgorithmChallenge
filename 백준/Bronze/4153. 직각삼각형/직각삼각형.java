import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {

        String input = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력값 받은 후 sort 진행.

        while(true) {
            String[] inputStr = br.readLine().split(" ");
            Integer[] numbers = new Integer[inputStr.length];

            for (int i = 0; i < inputStr.length; i++){
                numbers[i] = Integer.parseInt(inputStr[i]);
            }

            Arrays.sort(numbers, Collections.reverseOrder());

            int sum = Arrays.stream(numbers)
                    .mapToInt(Integer::intValue)
                    .sum();

            if (sum == 0){
                break;
            }

            int result = 0;

            if (numbers[0] * numbers[0] == numbers[1] * numbers[1] + numbers[2] * numbers[2]){
                System.out.println("right");
            } else{
                System.out.println("wrong");
            }

        }
        /*
        세변의 길이가 주어지고 이게 직각 삼각형인지 구분하시오.
        맞으면 right 출력
        틀리면 wrong 출력

        마지막 줄에는 000이 나옴.

        직각 삼각형임을 아는법

        가장 큰수의 제곱 = 두수의 제곱을 더한것과 같으면 right 아니면 wrong출력.
         */
    }
}
