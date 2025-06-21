import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class Main {

    public static void main(String[] args) throws IOException {

//        String input = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        int cnt = 0;

        ArrayList<Integer> intList = new ArrayList<>();

        for (int i = 0; i < 9; i++) {
            intList.add(Integer.parseInt(br.readLine()));
        }

        int max = Collections.max(intList);
        int index = intList.indexOf(max);
        System.out.println(max);
        System.out.println(index+1);


//        intList.sort(Comparator.reverseOrder());  [정렬하는방법]
//        int max = intList.stream().max(Integer::compare).get(); [최댓값 구하는방법]




    }
}
