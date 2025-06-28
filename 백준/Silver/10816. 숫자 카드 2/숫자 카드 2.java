import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    static int lowerBound(int[] arr, int target){
        int left = 0;
        int right = arr.length;

        while(left < right){
            int mid = (left + right) / 2;

            if(arr[mid] >= target){
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    static int upperBound(int[] arr, int target){
        int left = 0;
        int right = arr.length;

        while (left < right){
            int mid = (left + right) / 2;

            if (arr[mid] > target){
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    public static void main(String[] args) throws IOException {

        String input = "src/input.txt";
//      BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());

        int[] arrN = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int M = Integer.parseInt(br.readLine());

        int[] arrM = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();


        Arrays.sort(arrN);

        for (int target : arrM){
            int count = upperBound(arrN, target) - lowerBound(arrN, target);
            sb.append(count).append(" ");
        }

        System.out.println(sb.toString().trim());

        /*
        카드 N개시 정수 M개가 주어지면 M과 N비교후 몇개인지 출력
         */
    }
}
