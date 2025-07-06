import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {


//        String input = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int N = Integer.parseInt(br.readLine());
        int[] P = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        // [[3,1] [1,2] [4,3]..]
        List<int[]> list = new ArrayList<>();
        for (int i = 0; i < N; i++){
            list.add(new int[]{P[i], i});
        }

        list.sort(Comparator.comparingInt(a -> a[0]));


        int total = 0;
        int answer = 0;
        
        for (int[] pair : list){
            total += pair[0];
            answer += total;
        }

        System.out.println(answer);


        /*
        1 ~ N 번호 잇음
        pi분걸림
        돈 인출 최소시간

        // 빨리 뽑은 순서대로 sort하게 된다면, 빨리 뽑지 않을까?


         */

    }
}
