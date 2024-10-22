
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {

//        String file = "src/day5/소수_2581/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(file));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int M = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());
        ArrayList<Integer> primeNumList = new ArrayList<>();
//        소수?
        // M ~ N 까지 진행
        for (int i = M; i <= N; i++){
            boolean isPrimeNumber = true;
            // 루트i를 구하고,
            double currentNumber = Math.sqrt(i);

            for (int j = 2; j <= currentNumber; j++){
                if(i % j == 0){
                    isPrimeNumber = false;
                }
            }
            if (isPrimeNumber == true && i != 1){
                primeNumList.add(i);
            }
        }

        int sum = primeNumList.stream().mapToInt(Integer::intValue).sum();

//        System.out.println(primeNumList);
        if (primeNumList.size() == 0 ){
            System.out.println(-1);
        } else{
            System.out.println(sum);
            System.out.println(primeNumList.get(0));
        }


        /*
        자연수 M 과 N 이 주어지면, M 이상 N이하의 자연수중 소수인것을 모두 골라서
        이 소수의 합과 최솟값을 찾으시오.
        소수 = 1을 제외하고 본인외에 나누어지는게 없어야함.
         */
    }
}
