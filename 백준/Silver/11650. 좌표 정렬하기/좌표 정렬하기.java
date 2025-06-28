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

        for(int i = 0 ; i < N; i++){
            String [] line = br.readLine().split(" ");
            arr[i][0] = line[0];
            arr[i][1] = line[1];
        }

        Arrays.sort(arr, new Comparator<String[]>() {
            @Override
            public int compare(String[] o1, String[] o2) {
                int x1 = Integer.parseInt(o1[0]);
                int x2 = Integer.parseInt(o2[0]);
                int y1 = Integer.parseInt(o1[1]);
                int y2 = Integer.parseInt(o2[1]);

                if (x1 != x2){
                    return x1 - x2;
                } else {
                    return y1 - y2;
                }
            }
        });

        for (int i = 0; i < N; i++){
            System.out.println(arr[i][0] + " " + arr[i][1]);
        }

        /*
        점 N개가 주어짐.
        X가 증가하는순으로 -> X가 같으면 Y가 증가하는순으로 정렬

         */

    }
}
