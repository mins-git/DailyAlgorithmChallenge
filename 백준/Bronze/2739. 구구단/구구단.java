import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {

//        String input = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int resultNum = Integer.parseInt(br.readLine());

        int i = 1;

        while (i <= 9){
            System.out.println(resultNum + " * " + i + " = " + (resultNum*i));

            i++;
        }
    }
}
