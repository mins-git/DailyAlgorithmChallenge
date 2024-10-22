
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args ) throws IOException{

//        String file = "src/day4/소수_찾기_1978/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(file));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // 4
        String[] input = br.readLine().split(" ");
        ArrayList<Integer> numbers = new ArrayList<>(); // 1 3 5 7
        int result = 0;
        for (String str : input){
            numbers.add(Integer.parseInt(str));
        }

        for (int i = 0; i < numbers.size(); i ++){
            int num = numbers.get(i);
            boolean isPrimeNumber = true;
            double checkPrimeNumber = Math.sqrt(num);

            for (int j = 2; j <= checkPrimeNumber; j++){
                if (num % j == 0){
                    isPrimeNumber = false;
                    break;
                }
            }
            if (isPrimeNumber == true && num != 1){
                result +=1;
            }
        }

        System.out.println(result);

        /**
         * 주어진 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램 작성

         소수가 몇개?
         소수 ? 1을 제외하고 본인 외에 나누어지는게 없어야함.

         */

    }
}
