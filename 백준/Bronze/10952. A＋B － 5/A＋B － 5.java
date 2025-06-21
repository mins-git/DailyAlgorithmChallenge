import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

//        String input = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line;

        int result = -1;

        while ((line = br.readLine()) != null){

            if (result == 0){
                System.out.println(0);
            }

            String[] inputStr = line.split(" ");

            int a = Integer.parseInt(inputStr[0]);
            int b = Integer.parseInt(inputStr[1]);

            if(a == 0 && b == 0) {
                result = 0;
                continue;
            }

            System.out.println(a+b);

            result = -1;

        }


    }
}
