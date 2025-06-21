import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

//        String input = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line = br.readLine();
        String[] stringList = line.split(" ");

        int realResult = 0;

        for (int i =0; i<5; i++){
            int number = Integer.parseInt(stringList[i]);

            int result = number * number;

            realResult += result;
        }

        System.out.println(realResult % 10);

        /*
        컴퓨터마다 6자리의 고유번호를 매긴다.

        처음 5자리의 각 자리수의 제곱 한 후 더하고 10으로 나눈 나머지값 구하기.

         */

    }
}
