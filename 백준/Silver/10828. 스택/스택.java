import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {

    public static void main(String[] args) throws IOException {

        String input = "src/input.txt";
//        BufferedReader br= new BufferedReader(new FileReader(input));
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        Deque<Integer> deque = new ArrayDeque<>();

        for (int t = 0; t < T; t++){

            String[] inputStr = br.readLine().split(" ");
            String command = inputStr[0];

            switch (command){
                case "push":
                    deque.push(Integer.parseInt(inputStr[1]));
                    break;

                case "pop":
                    System.out.println(deque.isEmpty() ? -1 : deque.pop());
                    break;

                case "size":
                    System.out.println(deque.size());
                    break;

                case "empty":
                    System.out.println(deque.isEmpty() ? 1 : 0);
                    break;

                case "top":
                    System.out.println(deque.isEmpty() ? -1 : deque.peek());
                    break;
            }
        }

        /*

         */


    }
}
