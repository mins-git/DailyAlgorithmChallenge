import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Main {

    public static void main(String[] args) throws IOException {

        String input = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int N = Integer.parseInt(br.readLine());

        String[][] arr = new String [N][2];

        for (int i = 0; i < N; i++){
            String [] line = br.readLine().split(" ");
            arr[i][0] = line[0];
            arr[i][1] = line[1];
        }

        Arrays.sort(arr, Comparator.comparingInt(a -> Integer.parseInt(a[0])));

        for (int i = 0; i < N; i++){
            System.out.println(arr[i][0] + " " +arr[i][1]);
        }

        /*

         */
    }
}
