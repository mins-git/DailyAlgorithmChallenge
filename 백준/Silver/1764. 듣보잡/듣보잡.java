import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {


//        String input = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] NM = br.readLine().split(" ");
        int N = Integer.parseInt(NM[0]);
        int M = Integer.parseInt(NM[1]);

        int totalNM = N+M;

        Set<String> setN = new HashSet<>();
        for (int i = 0; i <N; i++){
            setN.add(br.readLine());
        }

        List<String> answer = new ArrayList<>();

        for(int i = 0; i < M; i++){
            String name = br.readLine();
            if (setN.contains(name)){
                answer.add(name);
            }
        }

        Collections.sort(answer);
        
        int answerSize = answer.size();
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < answerSize; i ++){
            sb.append(answer.get(i) + "\n");
        }

        System.out.println(answerSize);
        System.out.println(sb);



        /*
        듣도 못한사람
        보도 못한 사람

        듣도 보도 못한 사람의 명단 구해.
        중복이 없으면. set으로 그냥 계쏙 add 하면 되지않나?


         */

    }
}
