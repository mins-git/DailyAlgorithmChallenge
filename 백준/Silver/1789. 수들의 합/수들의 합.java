
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException{

//        String file = "src/baekJoon/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(file));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long S = Long.parseLong(br.readLine().trim());
        ArrayList<Long> resultList = new ArrayList<>(); //[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


        long sum = 0; // 210
        long k = 1;
        while(sum < S){ // 같으면 안됨
            resultList.add(k);
            sum += k; // sum에 k를 더해줌
            k ++; // k를 증가시킴
        }

        while(sum > S){
            if (resultList.contains(sum-S)){
                resultList.remove(Long.valueOf(sum-S));
                break;
            }
        }

        System.out.println(resultList.size());


    }
}
