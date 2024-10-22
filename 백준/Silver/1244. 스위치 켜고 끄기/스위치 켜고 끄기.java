import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 스위치 개수 입력
        int n = Integer.parseInt(br.readLine());
        // 스위치 상태 입력 (1: 켜짐, 0: 꺼짐)
        int[] switches = new int[n + 1]; // 1번부터 n번까지 사용하기 위해 n+1 크기로 배열 선언
        String[] input = br.readLine().split(" ");
        for (int i = 1; i <= n; i++) {
            switches[i] = Integer.parseInt(input[i - 1]);
        }

        // 남학생 수 입력
        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            String[] studentInput = br.readLine().split(" ");
            int gender = Integer.parseInt(studentInput[0]);
            int num = Integer.parseInt(studentInput[1]);

            if (gender == 1) { // 남학생
                // num의 배수 스위치 상태 변경
                for (int j = num; j <= n; j += num) {
                    switches[j] = switches[j] == 0 ? 1 : 0; // 0이면 1로, 1이면 0으로 변경
                }
            } else { // 여학생
                switches[num] = switches[num] == 0 ? 1 : 0; // 해당 스위치 상태 변경
                // 대칭으로 스위치 상태 변경
                for (int j = 1; j <= (n / 2); j++) {
                    if (num - j < 1 || num + j > n) break; // 범위 체크
                    if (switches[num - j] == switches[num + j]) {
                        switches[num - j] = switches[num - j] == 0 ? 1 : 0; // 상태 변경
                        switches[num + j] = switches[num + j] == 0 ? 1 : 0; // 상태 변경
                    } else {
                        break;
                    }
                }
            }
        }

        // 결과 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            sb.append(switches[i]).append(" ");
            if (i % 20 == 0) sb.append("\n"); // 20개마다 줄바꿈
        }
        System.out.println(sb.toString().trim());
    }
}
