

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

// A -> B
public class Main{

    // 뒤에 1을 추가하는 코드
    public static long stringPlusOne(long beforeInt) {
        String result = Long.toString(beforeInt) + "1";
        return Long.parseLong(result);
    }

    // 2를 곱할 코드
    public static long doubleTwo(long beforeInt){
        return beforeInt * 2;
    }

    public static int bfs(long A, long B){

        Queue <long[]> queue = new LinkedList<>();
        queue.add(new long[]{A,1}); // 숫자와 연산 횟수 저장

        while(!queue.isEmpty()){
            long[] current = queue.poll();
            long number = current[0];
            int steps = (int) current[1];

            // 목표값에 도달한 경우
            if (number == B) {
                return steps;
            }

            // 2를 곱한 값
            long doubled = doubleTwo(number);
            if (doubled <= B) {
                queue.add(new long[]{doubled, steps + 1});
            }

            // 뒤에 1을 추가한 값
            long appendedOne = stringPlusOne(number);
            if (appendedOne <= B) {
                queue.add(new long[]{appendedOne, steps + 1});
            }

        }
        return -1;
    }

    public static void main(String[] args) throws IOException {


//        String input = "src/baekJoon/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String [] inputAB = br.readLine().split(" ");

        long A = Long.parseLong(inputAB[0]);
        long B = Long.parseLong(inputAB[1]);


        long result= bfs(A,B);

        System.out.println(result);


        /*
        정수 A -> B로 변경한다면
        2를 곱하거나
        1을 수의 가장 오른쪽에 추가하거나 최솟값?

        A -> B로 꾸는데 필요한 연산의 최솟값?

        최솟값 : bfs를 사용해도 될것 같음.

         */

    }
}