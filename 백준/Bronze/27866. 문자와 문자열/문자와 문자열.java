import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {

//        String input = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String word = br.readLine();
        int wordNum = Integer.parseInt(br.readLine()) - 1;

        for (int i = 0; i < word.length(); i++){
            if (wordNum == i){
                System.out.println(word.charAt(i));
            }
        }


        // 단어의 i번째 수 출력

    }
}
