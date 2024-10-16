package algorithms.Java_Skill_Boost_Challenge.스위치_켜고_끄기_1244;


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {


        String filePath = "src/algorithms/Java_Skill_Boost_Challenge/스위치_켜고_끄기_1244/input.txt";
        BufferedReader br = new BufferedReader(new FileReader(filePath));


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


        // 학생수만큼 진행하면서 switchStatus 상태를 바꾸면됨.
        for (int i = 0; i < studentCount; i++){
            if (studentCommands[i][0] == 1) {
                // 배수로 switchStatus 변경해주기

            } else if (studentCommands[i][0] == 2){

            }
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

}
