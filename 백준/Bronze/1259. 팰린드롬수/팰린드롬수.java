import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {

        String input = "src/input.txt";
//      BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while(true){
            int inputInt = Integer.parseInt(br.readLine());
            if(inputInt == 0){
                break;
            }

            List<Integer> digits = new ArrayList<>();
            for (char c : String.valueOf(inputInt).toCharArray()){
                digits.add(c - '0');
            }

            // [1,2,4,2,1]
            boolean result = true;

            for (int i = 0; i < digits.size() / 2; i ++){

                if (!digits.get(i).equals(digits.get(digits.size() -1 -i))){
                    result = false;
                    break;
                }
            }

            if (result){
                System.out.println("yes");

            } else System.out.println("no");

        }

        /*
        앞뒤로 읽어도 똑같으면 팰린드롬이라고함.

        앞에 0이 올 일은 없음.

        팰린드롬 여부에 따라서
        yes or no 출력.

        팰린드롬 여부 체크방법:


         */


    }
}
