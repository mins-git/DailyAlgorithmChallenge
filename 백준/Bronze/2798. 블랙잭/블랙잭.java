import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {

        String input = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] inputInt = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int N = inputInt[0];
        int M = inputInt[1];

        int[] cards = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        // 오름차순 정렬
        Arrays.sort(cards);

        int answer = 0;

        for(int i = 0; i < N - 2; i++){
            int left = i + 1;
            int right = N - 1;

            while (left < right){
                int sum = cards[i] + cards[left] + cards[right];

                if(sum > M){
                    right --;
                } else {
                    if(sum > answer){
                        answer = sum;
                    }
                    
                    if(sum == M){
                        break;
                    }
                    left ++;
                }
            }
        }
        System.out.println(answer);

        /*
        카드합 21 넘지 않도록 카드 합 최대한 크게.

        N장의 카드를 바닥에 놓고 M을 외침

        N장의 카드 중 3장을 고른 합은 M을 넘지 않으면서 M과 최대한 가까워야함.

        N장의 카드에 써져있는 숫자가 주어지면, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구하시오.

        3장을 뽑아서 M과 최대한 가까운 수를 구하는방법?
        3장을 뽑는 조합?..?
         */
    }
}
