import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

//        String file = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(file));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String A = br.readLine();
        String B = br.readLine();
        String C = br.readLine();
        

        System.out.println(Integer.parseInt(A) + Integer.parseInt(B) - Integer.parseInt(C));
        System.out.println(Integer.parseInt(A+B)-Integer.parseInt(C));

    }
}