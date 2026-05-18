import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case ++){

            // 10개의 수를 입력 받아 그 중에서 홀수만 더한 값을 출력하는 프로그램 작성.
            // 각 수는 0 이상 10000 이하의 정수 이다.

            // 홀수 = > 2로 끝까찌 나누었을때에 나머지가 1이 되어야함.

            // 리스트 안에 숫자 넣고.
            ArrayList<Integer> list = new ArrayList<>();
            for (int i = 0; i < 10; i++){
                list.add(sc.nextInt());
            }

            int result = 0;

            for (int j = 0; j< 10; j++){
                if (list.get(j) % 2 == 1){
                    result += list.get(j);
                }
            }

            System.out.println("#"+ test_case + " " + result);

        }

    }
}