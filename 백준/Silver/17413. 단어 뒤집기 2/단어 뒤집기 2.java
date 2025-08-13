import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {

        String file = "src/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(file));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String inputStr = br.readLine();

//        System.out.println(inputStr);
//        <ab cd>ef gh<ij kl>



        // 출력할 값.
        String result = "";
        int inputStrlen = inputStr.length(); // 19 맞음
        boolean isTrue = false;
        String preResult = "";

        // 단어의 길이만큼 순회를 하면서 ->
        for (int i = 0; i < inputStrlen; i++){

            Character S = inputStr.charAt(i);

            // if "<" 가 현재 char와 같다면 boolean 값을 true 로 만들기
            if (S.equals('<')) {
                isTrue = true;
                // 태그 시작 전 남은 단어 뒤집어야함.
                for (int j = preResult.length() - 1; j >= 0; j--) {
                    result += preResult.charAt(j);
                }
                preResult = "";
                result += S;
                continue;
            }

            if (isTrue) { // isTrue 값이 true이면?
                result += S;
                if (S == '>') { // 태그 종료
                    isTrue = false;
                }
            } else { // is True 값이 false이면?

                // 만약 띄어쓰기가 있다면,
                if (S.equals(' ')) {
                    for (int j = preResult.length() - 1; j >= 0; j--) {
                        result += preResult.charAt(j);
                    }
                    preResult = "";
                    result += ' ';
                } else {
                    preResult += S;
                }
            }

        }
        for (int j = preResult.length() - 1; j >= 0; j--) {
            result += preResult.charAt(j);
        }

        System.out.println(result);

        /*
        단어의 길이만큼 순회를 하면서 ->

        if "<" 가 현재 char와 같다면 boolean 값을 true 로 만들기 {

        }

        if boolean값이 false이면 {
            단어를 하나하나 str에 저장해야됨.
            그 후 띄어쓰기를 만나면, result에 그대로 붙여넣기.
        } if boolean값이 true이고, ">"를 만나게 되면, {

        } if boolean값이 true 값이면{
            if 다음값이 ">"라고 한다면, {
                boolean값을 false로 만들고
                result에 ">"를 붙여넣기
                다음 회차로 돌려버리기
            }
            result에 값이 붙여넣기.
        }


        result 출력하기
         */



        /*

        문자열 S가 주어짐. 단어만 뒤집으려고함.

        소문자는 a-z
        숫자는 0-9
        공백 ''
        특문 < , >

        <>가 번갈아 있는경우 <가 먼저 등장함.(두 문자의 개수가 같음)
        <> 사이에는 알파벳 소문자 or 띄어쓰기만 있음.

        태그를 제외하고, 글자 뒤집기 진행.
        태그가 있으면 태그만큼 그대로  출력하면되고, 그 외에는 뒤집기

         */

    }
}