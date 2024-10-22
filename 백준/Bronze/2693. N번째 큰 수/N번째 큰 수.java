
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {

//        String file = "src/day4/N번째_큰_수_2693/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(file));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tc = Integer.parseInt(br.readLine());

        for (int i = 0; i < tc; i++){
            String[] findThird = br.readLine().split(" "); // {} string list에 담아주고
            List<Integer> intList = new ArrayList<>();
            for (int j = 0; j < findThird.length; j ++){
                intList.add(Integer.parseInt(findThird[j])); // [1, 2, 3, 4, 5, 6, 7, 8, 9, 1000]
            }
            Collections.sort(intList);

            System.out.println(intList.get(7));
        }


        /*
        배열 10의 크기 A가 있다면, 3번째 큰 값을 출력하는 프로그램 작성

         */

    }
}
