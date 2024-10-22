package algorithms.Java_Skill_Boost_Challenge.스위치_켜고_끄기_1244;


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {


        String filePath = "src/algorithms/Java_Skill_Boost_Challenge/스위치_켜고_끄기_1244/input.txt";
        BufferedReader br = new BufferedReader(new FileReader(filePath));
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int switchCount = Integer.parseInt(br.readLine());
        int[] switchStatus = new int[switchCount];

        String[] switchCodeStrings = br.readLine().split(" ");
        for (int i = 0; i< switchCount; i++){
            switchStatus[i] = Integer.parseInt(switchCodeStrings[i]);
        }

        int studentCount = Integer.parseInt(br.readLine());
        int [][] studentCommands = new int[studentCount][2];

        for (int i = 0; i < studentCount; i++){
            String[] parts = br.readLine().split(" ");
            studentCommands[i][0] = Integer.parseInt(parts[0]);
            studentCommands[i][1] = Integer.parseInt(parts[1]);
        }
//        System.out.println(Arrays.deepToString(studentCommands)); // [[1, 3], [2, 3]]


//        // 학생수만큼 진행하면서 switchStatus 상태를 바꾸면됨.
//        for (int i = 0; i < studentCount; i++){
//            if (studentCommands[i][0] == 1) {
//                // studentCommands[i][1]배수로 switchStatus 변경해주기
//                int number = studentCommands[i][1]; // 3 이저장될것임.
//
//                if(number == 1){
//                    while(number < switchCount){
//
//                        if (switchStatus[number-1] == 0){
//                            switchStatus[number-1] = 1;
//                        } else{
//                            switchStatus[number-1] = 0;
//                        }
//                        number ++ ; // 자바에서도 사용 가능.
//                    }
//                } else {
//
//                    while(number < switchCount){
//
//                        if (switchStatus[number-1] == 0){
//                            switchStatus[number-1] = 1;
//                        } else{
//                            switchStatus[number-1] = 0;
//                        }
//                        number += studentCommands[i][1] ; // 자바에서도 사용 가능.
//                    }
//                }
//            // 만약 여자라면은,
//            } else if (studentCommands[i][0] == 2){
//                int number2 = studentCommands[i][1];
//                number2 --;
//                // 본인외 대칭되게 스우치를 모두 바꿈.
////                본인 대칭되게 양쪽 스위치 바꿈
//                // 만약 좌우가 똑같으면 다음것 체크, 또 그다음것이 독같으면 좌우체크.
//                // if studentCommands[i][1] == 1 or 마지막 번호면 이면 본인만 바꾸고
//
//                // 두번째 숫자가 1이거나 switchCount와 같다면,
//                int cnt = 0;
//                int numberi = 1;
//
//
//                while ((number2-numberi) >= 0 && (number2+numberi) < switchCount){
//                    // 본인 number2의 앞뒤 인덱스 값이 같으면,
//                    if (switchStatus[number2-(numberi)] == switchStatus[number2+numberi]){
//                        cnt += 1;
//                        numberi += 1;
//                    } else if (cnt == 0){
//                        if (switchStatus[number2-1] == 1){
//                            switchStatus[number2-1] = 0;
//                            break;
//                        } else if (switchStatus[number2-1] == 0) {
//                            switchStatus[number2-1] = 1;
//                            break;
//                        }
//                    } else{
//                        // 앞뒤값이 같지않고, cnt의 값이 0이 아니면,
//                        break;
//                    }
//                }
//                // cnt에 어떠한 값이 있겠지? number2-cnt ~ number2+cnt 만큼 위치 내용들 변경
//                // (number2+cnt) - (number2-cnt) + 1 의 횟수만큼 반복해서 안에 내용을 바꾸면됨.
//
//                for (int j = (number2-cnt);  j <= (number2+cnt); j++) {
//                    // 반복할 코드 작성
//                    if (switchStatus[j] == 0){
//                        switchStatus[j] = 1;
//                    } else{
//                        switchStatus[j] = 0;
//                    }
//                }
//            }
//        }

        String result = String.join(" ", Arrays.stream(switchStatus)
                .mapToObj(String::valueOf)
                .toArray(String[]::new)
        ).trim();

        System.out.println(result);

//        System.out.println(Arrays.toString(switchStatus)); [1, 0, 0, 0, 1, 1, 0, 1]
    }
}
    /*
    1번 부터 연속적으로 번호가 붙어있는 스위치가 있다. 스위치 켜져있거나 꺼져있는 상태.
    1은 켜짐 0은 꺼짐
    남학생 : 스위치 번호가 자기 받은 수의 배수면, 스위치 : 상태 바꿈.
    여학생 : 본인외 대칭되게 스우치를 모두 바꿈.
            - 양쪽이 다르면 본인을 바꾸면됨.
    입력 첫줄 : 스위치 개수
    둘째 : 스위치 상태
    셋째: 학생수 주어짐
    [ 남학생 1/ 여학생 2 ] / [받은 스위치 번호] : 학생수만큼 주어짐
    */


