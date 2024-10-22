

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static void main (String[] args) throws IOException{

//        String file = "src/day5/쉽게_푸는_문제_1292/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(file));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputArr= br.readLine().split(" ");
        ArrayList<Integer> input = new ArrayList<>();

        for (int i = 0; i < inputArr.length; i++){
            input.add(Integer.parseInt(inputArr[i]));
        }

        ArrayList<Integer> numberList = new ArrayList<>();

        int j = 0;
        int a = 1;
        while (input.get(1) > numberList.size()){
            for (int f = 1; f <= a; f++ ){ //
                numberList.add(a);
            }
            a += 1;
            j += 1;
            // 1 22 333 4444 55555 만들어야함.
        }

//        System.out.println(numberList); // [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        int resultSum = 0;
        for (int k = input.get(0); k <= input.get(1); k++){
            resultSum += numberList.get(k-1);
        }

        System.out.println(resultSum);



        /*
        동호는 내년에 초등학교 입학함. 수학 선행 학습을 위해 쉽게 푸는 문제를 동호에게 줌.

        1을 한번 2를 두번 3을 세번 122334445555 수열만들고 일정구간의 합을 구하는것.

        첫번째줄에 구간의 시작과 끝을 나타내는 정수 주어짐.
        1 22 333 4444 55555





         */

    }
}
