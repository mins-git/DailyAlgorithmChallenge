package algorithms.Java_Skill_Boost_Challenge.수_이어나가기_2635;

import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {

        String filePath = "src/algorithms/Java_Skill_Boost_Challenge/수_이어나가기_2635/input.txt";
        BufferedReader br = new BufferedReader(new FileReader(filePath));
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int maxLength = 0; // 최대길이
        int resultA = 0; // 두 번째 수
        ArrayList<Integer> bestSequence = new ArrayList<>();


        // 첫번째 수는 n으로 고정하고 j로 시작하면됨.
        for(int j = n; j >= 0; j--){
            int a = n; // 첫번째 수는 n
            int b = j; // 두번재 수는 j

            ArrayList<Integer> currentSequence = new ArrayList<>();
            currentSequence.add(a);
            currentSequence.add(b);
            int length = 2; // 이미 두개(n과 다음수)가 사용되었으니 2로 시작함.

            while(true){
                int c = a-b; // 다음 수
                if(c<0) break;
                currentSequence.add(c); //현재 수열에 추가
                a = b; // a를 b로 갱신
                b = c; // b를 c로 갱신
                length++; // 길이증가. n까지 못갔으니 숫자 계속추가.
            }

            if (length > maxLength){
                maxLength = length;
                resultA = j;
                bestSequence = currentSequence;
            }
        }

        System.out.println(maxLength);
        System.out.println(String.join(" ", bestSequence.stream().map(String::valueOf).toArray(String[]::new)));
    }

        /*
        1. 첫번째 수 양의 정수가 주어짐.
        2. 양의 정수중에서 하나 선택,
        3. 세번째 부터 이후에 나오는 모든 수는 앞의 수에서 앞의수를 빼서 만듦.
        ex) 세번째 수는 첫번째 수 - 두번째 수, 네번째 수 = 두번재 수 - 세번째 수
        4. 음의 정수가 만들어지면 음의 정수를 버리고 더이상 수를 만들지 않음.

        입력으로 첫번재 수가 주어지면 이 수에서 위의 규칙으로 만들어지는 최대 개수의 수를 구하는 프로그램 작성.
        최대 개수의 수들이 여러 개 일때 그중 하나의 수들만 출력하면 됨.


        브루트 포스 알고리즘으로
        1부터~ n-1까지 다빼보는걸 진행해보고 최대숫자의 값을 두자.
         */

}


