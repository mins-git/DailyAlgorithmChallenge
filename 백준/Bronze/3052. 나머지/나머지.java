
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException {

//        String input = "src/baekJoon/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayList<Integer> number = new ArrayList<>();

        for (int i =0; i< 10; i++){
            number.add(Integer.parseInt(br.readLine()));
        }

        Set<Integer> result = new HashSet<>();

        for (int j =0; j<10; j++){
            result.add((number.get(j) % 42));
        }
        
        System.out.println(result.size());
    }
}
