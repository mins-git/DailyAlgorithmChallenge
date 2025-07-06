import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    public static void main(String[] args) throws IOException {

        String input = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        boolean[] set = new boolean[21];

        int M = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        while(M-- > 0){

            String[] cmd = br.readLine().split(" ");
            String operation = cmd[0];

            if (operation.equals("add")){
                int x = Integer.parseInt(cmd[1]);
                set[x] = true;
            } else if (operation.equals("remove")){
                int x = Integer.parseInt(cmd[1]);
                set[x] = false;
            } else if (operation.equals("check")){
                int x = Integer.parseInt(cmd[1]);
                sb.append(set[x] ? "1\n" : "0\n");

            } else if (operation.equals("toggle")){
                int x = Integer.parseInt(cmd[1]);
                set[x] = !set[x];
            } else if (operation.equals("all")){
                for (int i = 1; i <=20; i++){
                    set[i] = true;
                }
            } else  if (operation.equals("empty")){
                for (int i = 1; i <= 20; i++) set[i] = false;
            }
        }
        
        System.out.print(sb);

        /*
        공집합 S가 주어짐.

        add :

         */

    }
}
