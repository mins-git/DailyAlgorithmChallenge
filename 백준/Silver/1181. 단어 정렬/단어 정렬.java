import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        String input = "src/input.txt";
//      BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 13
        int N = Integer.parseInt(br.readLine());

        Set<String> set = new HashSet<>();

        for (int i = 0; i < N; i++){
            String word = br.readLine();
            set.add(word);
        }

        List<String> wordList = new ArrayList<>(set);

        Collections.sort(wordList, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                if (o1.length() != o2.length()){
                    return o1.length() - o2.length();
                } else {
                    return o1.compareTo(o2);
                }
            }
        });


        for (String w : wordList){
            System.out.println(w);
        }

        br.close();


        /*
        단어 정렬

        N개의 단어가 들어오면 정렬하세요.

        길이가 짧은것부터.
        길이가 같으면 사전순

        중복된 단어는 제거 필요.
         */
    }
}
