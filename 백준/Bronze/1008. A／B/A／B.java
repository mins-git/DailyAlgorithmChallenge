import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {

//        String input = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String[] inputString = br.readLine().split(" ");

        double result = Double.parseDouble(inputString[0]) / Double.parseDouble(inputString[1]);

        System.out.println(result);
    }
}
