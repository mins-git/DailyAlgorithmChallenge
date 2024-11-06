import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

// 9375 패션왕 신해빈
public class Main {
    public static void main(String[] args) throws IOException {

//      String file = "src/baekJoon/input.txt";
//        BufferedReader br =  new BufferedReader(new FileReader(file));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCnt = Integer.parseInt(br.readLine());

        for (int i = 0; i < testCnt; i++){
            int clothingCnt = Integer.parseInt(br.readLine());
            Map<String, Integer> categoryMap = new HashMap<>();

            for (int j = 0; j<clothingCnt; j++){
                String[] clothes = br.readLine().split(" ");  // 공백으로 나누어 배열에 저장
                String category = clothes[1];

                categoryMap.put(category, categoryMap.getOrDefault(category, 0) + 1);
            }

            int result = 1;
            // 모든 카테고리에 대해 의상 선택 방법의 수 계산
            for (int count : categoryMap.values()) {
                result *= (count + 1);  // 의상 수 + 1 (선택하지 않음도 포함)
            }

            // 선택하지 않는 경우를 제외하기 위해 1을 뺌
            System.out.println(result - 1);

        }


        /*
        해빈이는 같은 조합을 다음날에 입지 않음.
        알몸이 아닌 상태로 며칠동안 밖에 돌아다닐 수 있을까?
         */


    }
}