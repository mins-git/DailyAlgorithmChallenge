import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.SQLOutput;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

//        String input = "src/baekJoon/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[][] people = new int[N][2];

        for (int i =0; i < N; i++){
            String[] line = br.readLine().split(" ");
            people[i][0] = Integer.parseInt(line[0]);
            people[i][1] = Integer.parseInt(line[1]);
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i <N; i++){
            int rank = 1;
            for(int j = 0; j < N ; j++){

                if(people[j][0] > people[i][0] && people[j][1] > people[i][1]){
                    rank++;
                }
            }
            sb.append(rank).append(" ");
        }

        System.out.println(sb.toString().trim());
        /*
        두 사람의 덩치를 키와 몸무게, 두 값으로 표현, 등수 매김
        덩치 등수 구하기
         */
    }
}


