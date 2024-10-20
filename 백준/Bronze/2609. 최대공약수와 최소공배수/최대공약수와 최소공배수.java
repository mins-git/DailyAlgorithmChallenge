import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.io.InputStreamReader;
public class Main {
    // 최대 공약수
    public static int gcd(int a, int b){
        if (b == 0){
            return a;
        }
        return gcd(b, a % b);
    }

    public static int lcm(int a, int b){
        return a * b / gcd(a,b);

    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String [] inputString = br.readLine().split(" ");
        List<Integer> input = new ArrayList<>();


        input.add(Integer.parseInt(inputString[0]));
        input.add(Integer.parseInt(inputString[1]));

//        System.out.println(input); // [24, 18]

        System.out.println(gcd(input.get(0), input.get(1)));
        System.out.println(lcm(input.get(0), input.get(1)));

        /*
        두 개의 자연수를 입력받아서 최대 공약수와 최소 공배수를 출력하시오.

         */


    }
}
