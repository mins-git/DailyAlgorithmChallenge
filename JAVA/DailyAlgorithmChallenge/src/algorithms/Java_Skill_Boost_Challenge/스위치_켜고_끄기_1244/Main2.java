package algorithms.Java_Skill_Boost_Challenge.스위치_켜고_끄기_1244;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.Collectors;

public class Main2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int switchCount = Integer.parseInt(br.readLine());
        int[] switchStatus = new int[switchCount];

        String[] switchCodeStrings = br.readLine().split(" ");
        for (int i = 0; i < switchCount; i++) {
            switchStatus[i] = Integer.parseInt(switchCodeStrings[i]);
        }

        int studentCount = Integer.parseInt(br.readLine());
        int[][] studentCommands = new int[studentCount][2];

        for (int i = 0; i < studentCount; i++) {
            String[] parts = br.readLine().split(" ");
            studentCommands[i][0] = Integer.parseInt(parts[0]);
            studentCommands[i][1] = Integer.parseInt(parts[1]);
        }

        // 학생 수만큼 진행하면서 switchStatus 상태를 바꿈
        for (int i = 0; i < studentCount; i++) {
            int gender = studentCommands[i][0]; // 1: 남학생, 2: 여학생
            int number = studentCommands[i][1]; // 스위치 번호

            if (gender == 1) {
                // 남학생: 받은 수의 배수로 스위치 상태 변경
                for (int j = number; j <= switchCount; j += number) {
                    switchStatus[j - 1] = switchStatus[j - 1] == 0 ? 1 : 0;
                }
            } else if (gender == 2) {
                // 여학생: 대칭으로 스위치 상태 변경
                int number2 = number - 1; // 배열 인덱스를 위해 1을 뺌
                int left = number2, right = number2;

                // 좌우가 대칭일 때만 확장
                while (left >= 0 && right < switchCount && switchStatus[left] == switchStatus[right]) {
                    left--;
                    right++;
                }

                // 대칭 범위 내 스위치 상태 반전
                for (int j = left + 1; j < right; j++) {
                    switchStatus[j] = switchStatus[j] == 0 ? 1 : 0;
                }
            }
        }

        // 결과 출력
        String result = Arrays.stream(switchStatus)
                .mapToObj(String::valueOf)
                .collect(Collectors.joining(" ")); // 공백으로 연결
        System.out.println(result); // 줄 바꿈 추가
    }
}
