package baekJoon;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;

public class Main{
    public static void main(String[] args) throws IOException {
//        String file = "src/baekJoon/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(file));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] inputStr = br.readLine().split(" ");
//        System.out.println(inputStr); 3 4
        ArrayList<Integer> inputNM = new ArrayList<>();
        ArrayList<String> notListen = new ArrayList<>();
        ArrayList<String> notLook = new ArrayList<>();

        for (int i = 0; i < inputStr.length; i++){
            inputNM.add(Integer.parseInt(inputStr[i]));
        }
//        System.out.println(inputNM.get(0).getClass().getName());
        int sum = inputNM.get(0) + inputNM.get(1);

        for (int j = 0; j < sum; j ++){
            if(j <= (inputNM.get(0)-1)){
                notListen.add(br.readLine());
            } else {
                notLook.add(br.readLine());
            }
        }

//        System.out.println(notListen); [ohhenrie, charlie, baesangwook]
//        System.out.println(notLook); [obama, baesangwook, ohhenrie, clinton]
        ArrayList<String> notListenLook = new ArrayList<>(notListen);
        notListenLook.retainAll(notLook);

//        System.out.println(notListenLook);

        Collections.sort(notListenLook);

        System.out.println(notListenLook.size());
        for (int z =0; z < notListenLook.size(); z++){
            System.out.println(notListenLook.get(z));
        }
    }
}




























//
//import java.io.BufferedReader;
//import java.io.FileReader;
//import java.io.IOException;
//import java.lang.reflect.Array;
//import java.util.ArrayList;
//import java.util.Arrays;
//import java.util.List;
//
//public class Main{
//
//    // n: 전체 숫자의 개수, targetNum: 목표, list
//    public static List<List<Integer>> combineTarget(int n, int targetNum, ArrayList<Integer> value){
//        List<List<Integer>> result = new ArrayList<>();
//        int cnt = 0;
//        backtrack(result, new ArrayList<>(), );
//        return result;
//    }
//
//    // result: 저장할 List 2차원 배열, num: 현재 숫자의합, cnt: 현재 조합 개수, targetNum: 목표Num, start: 시작지점, n: 전체 개수
//    private static void backtrack(List<List<Integer>> result, List<Integer> temList, int num ,int cnt, int targetNum, int start, int n, ArrayList<Integer> value){
//        if(num == targetNum){
//            cnt += 1;
//            return;
//        }
//
//        for(int i = start; i <=n; i++){
//            num +=
//            backtrack(result, temList,);
//        }
//    }
//
//
//    private static void backtrack(List<List<Integer>> result, List<Integer> temList, int start, int n, int k){
//        if(temList.size() == k ){
//            result.add(new ArrayList<>(temList));
//            return;
//        }
//        for (int p = start; p <= n; p++){
//            temList.add(p);
//            backtrack(result, temList, p+1, n, k);
//            temList.remove(temList.size()-1);
//        }
//    }
//
//
//
//    public static void main(String [] agrs) throws IOException{
//
//        String file = "src/baekJoon/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(file));
//
//        String[] input = br.readLine().split(" ");
//        Integer[] intInput = new Integer[2];
//        ArrayList<Integer> value = new ArrayList<>();
//
//        for (int i = 0; i < input.length; i ++){
//            intInput[i] =  Integer.parseInt(input[i]);
//        }
////        System.out.println(Arrays.toString(intInput));
//
//        for (int j = 0; j < intInput[0]; j ++){
//            value.add(Integer.parseInt(br.readLine()));
//        }
////        System.out.println(value);
//
//
//
//
//        /*
//        n가지 종류의 동전이 존재. 각각의 동전이 나타내는 가치는 다르다
//        적당히 사용해서 가치의 합이 k원 그 경우의 수를 구하시오.
//         */
////
//    }
//
//}