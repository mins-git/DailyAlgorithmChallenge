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
        StringBuilder sb = new StringBuilder();

        String[] inputStr = br.readLine().split(" ");
        int N = Integer.parseInt(inputStr[0]);
        int K = Integer.parseInt(inputStr[1]);

        Deque<Integer> deque = new ArrayDeque<>();
        for (int i = 1; i <= N; i++){
            deque.offerLast(i);
        }

        sb.append("<");

        while(!deque.isEmpty()){
            for (int i = 1; i < K; i++){
                deque.offerLast(deque.pollFirst());
            }

            sb.append(deque.pollFirst());
            if(!deque.isEmpty()){
                sb.append(", ");
            }
        }

        sb.append(">");
        System.out.println(sb.toString());

        /*
        1 ~ N번까지 원으로 앉아있음.
        K번째 사람을 제거함.

        N명의 사람이 모두 제거될때까지 반복됨.
         */
    }
}
