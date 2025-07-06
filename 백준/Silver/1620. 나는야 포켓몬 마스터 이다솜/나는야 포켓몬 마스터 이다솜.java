import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {


        String input = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        String[] NM = br.readLine().split(" ");
        int N = Integer.parseInt(NM[0]);
        int M = Integer.parseInt(NM[1]);

        String[] bookArr = new String[N];
        Map<String, Integer> bookMap = new HashMap<>();

        for (int i = 0; i < N; i++) {
            String name = br.readLine();
            bookArr[i] = name;
            bookMap.put(name, i + 1);
        }


        StringBuilder sb = new StringBuilder();


        for (int i = 0; i < M; i++){
            String Q = br.readLine();

            try{
                int num = Integer.parseInt(Q);
                sb.append(bookArr[num - 1]).append("\n");

            } catch (NumberFormatException e) {
                sb.append(bookMap.get(Q)).append("\n");
            }
        }

        System.out.print(sb);
        
        /*
        가지고 있는 도감에서 -> 포켓몬 번호 말하거나, 이름을 말함

         */
    }
}
