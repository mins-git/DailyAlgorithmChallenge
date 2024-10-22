package algorithms.Java_Skill_Boost_Challenge.스위치_켜고_끄기_1244;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;


public class Main2 {
    public static void main(String[] args) throws IOException {

//        String file = "src/algorithms/Java_Skill_Boost_Challenge/스위치_켜고_끄기_1244/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(file));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 스위치 카운트
        int switchCnt = Integer.parseInt(br.readLine());

        // 스위치 상태
        String[] preSwitchStatus = br.readLine().split(" ");
        ArrayList<Integer> switchStatus = new ArrayList<>(); // [0, 1, 0, 1, 0, 0, 0, 1]

        for (int z = 0; z < preSwitchStatus.length; z++){
            switchStatus.add(Integer.parseInt(preSwitchStatus[z]));
        }

        // 학생수
        int studentCnt = Integer.parseInt(br.readLine());
        ArrayList<ArrayList<Integer>> studentStatus = new ArrayList<>();
        for(int y = 0; y < studentCnt; y++){
            ArrayList<Integer> preInput = Arrays.stream(br.readLine().split(" "))
                    .map(Integer::parseInt)
                    .collect(Collectors.toCollection(ArrayList::new));
            studentStatus.add(preInput);
        }

//        System.out.println(studentStatus); // [[1, 3], [2, 3]]
//        System.out.println(studentStatus.size()); //2
        // 남학생 코드 변경

        for (int i = 0; i < studentStatus.size(); i++){
            int femaleOrMale = studentStatus.get(i).get(0);
            int switchNumber = studentStatus.get(i).get(1);

            // 남학생 스위치라면
            if(femaleOrMale == 1){
                // 현재 스위치 번호
                int currentSwitch = switchNumber;

                // 현재 스위치 번호 ~ 스위치 카운트전까지만
                for (int j = switchNumber; j <= switchCnt; j += switchNumber){
                    switchStatus.set(j-1, (switchStatus.get(j-1) == 0) ? 1 : 0);
                }
            }
            else if (femaleOrMale == 2) {
                int left = switchNumber - 1; // 여학생의 스위치 번호는 1부터 시작하므로 -1
                int right = switchNumber - 1;

                // 스위치 상태 변경
                switchStatus.set(switchNumber - 1, (switchStatus.get(switchNumber - 1) == 0) ? 1 : 0);

                // 좌우 대칭 스위치 상태 변경
                while (left > 0 && right < switchCnt - 1) {
                    if (switchStatus.get(left - 1) == switchStatus.get(right + 1)) {
                        switchStatus.set(left - 1, (switchStatus.get(left - 1) == 0) ? 1 : 0);
                        switchStatus.set(right + 1, (switchStatus.get(right + 1) == 0) ? 1 : 0);
                        left--;
                        right++;
                    } else {
                        break;
                    }
                }
            }

//            // 여학생 스위치라면
//            if (femaleOrMale == 2){
//                int k = 1;
//                while (switchNumber-k > 1 && switchNumber+k < switchStatus.size()) {
//                    // 현재 스위치 넘버
//                    if (switchStatus.get(switchNumber-k-1) != switchStatus.get(switchNumber+k-1)){
//                        switchStatus.set(switchNumber-1 ,(switchStatus.get(switchNumber-1) == 0 ) ? 1 : 0);
//                        break;
//                    }
//                    k +=1;
//                }
//
//                if (k != 1) {
//                    for (int start = switchNumber - k; start < k + switchNumber; start++) {
//                        switchStatus.set(start - 1, (switchStatus.get(start - 1) == 0) ? 1 : 0);
//                    }
//                } else if (k == 1){
//                    switchStatus.set(switchNumber-1, (switchStatus.get(switchNumber-1)==0) ? 1: 0);
//                }
//            }

        }

        StringBuilder output = new StringBuilder();

        for (int l = 0; l < switchStatus.size(); l++){
            output.append(switchStatus.get(l)).append(" ");

            if ((l+1) % 20 == 0) output.append("\n"); // 20개마다 줄바꿈

        }
        System.out.println(output.toString().trim());



        /*
        1부터 연속적으로 번호가 붙어있는 스위치가 있음.

        남학생은 자신의 배수로 스위치의 상태를 바꿈.

        여학생은 좌우 대칭이면서 가장 많은 스위치 포함하는 구간을 찾아서 모두 상태를 바꿈.
        없으면 본인 바꿈

         */

    }
}
