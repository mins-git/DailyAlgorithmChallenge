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

        int N = Integer.parseInt(br.readLine());

        Deque<Integer> deque = new ArrayDeque<>();

        for (int i = 1; i <= N; i++) {
            deque.addLast(i);
        }

        while(deque.size() != 1){
            deque.pollFirst();

            int add = deque.removeFirst();
            deque.addLast(add);
        }

        System.out.println(deque.pollFirst());


        /*
        N장의 카드

        1장 바닥에 버리고 제일 앞에걸 제일뒤로 옮김

        제일 마지막에 남는 카드는?
         */
    }
}
