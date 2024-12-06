package baekJoon;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

// 단지 번호 붙이기
public class Main {
    public static int[] stringToIntArray(String str){
        int[] arr = new int[str.length()];
        for (int i = 0; i< str.length(); i++){
            arr[i] = str.charAt(i) - '0';
        }
        return arr;
    }

    private static int dfs(int[][] aptList, int r, int c, int[] dr, int[] dc, int N){
        aptList[r][c] = 0; // 방문처리
        int cnt = 1; // 현재 노드 포함

        // 델타 진행
        for (int d = 0; d < 4; d++){
            int nr = r + dr[d];
            int nc = c+ dc[d];

            // 범위를 벗어나지 않고 아직 방문하지 않은 경우
            if(nr >=0 && nr < N && nc >=0 && nc < N && aptList[nr][nc]==1 ){
                cnt += dfs(aptList, nr, nc, dr, dc, N);
            }
        }
        return cnt;
    }

    public static void main(String[] args) throws IOException {
//        String input = "src/baekJoon/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[][] aptList = new int[N][N];

        for (int i = 0; i < N; i++){
            String line = br.readLine();
            aptList[i] = stringToIntArray(line);
        }

        List<Integer> components = new ArrayList<>();

        int[] dr = {0, 1, 0, -1}; //오아왼위
        int[] dc = {1, 0, -1, 0}; // 오아왼위

        // 순회
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (aptList[i][j] == 1){
                    int cnt = dfs(aptList, i, j, dr, dc, N);
                    components.add(cnt);
                }
            }
        }

        Collections.sort(components);
        System.out.println(components.size());
        components.forEach(System.out::println);


        /*
        몇개의 리스트가 있을지 체크해야됨.

        방법1)
//   제외     1. 방문여부 확인을 위한 방문 list 생성: 해당 리스트는 숫자가 1이었는데 방문처리된 곳을 담고있음.

        1. 만약 현재 위치가 1이면
        2-1: 델타 진행시 오아왼위로 위의 가지수를 체크해서 DFS 진행하면됨.
        2-2: DFS 과정중 방문처리는 1을 0으로 변경해주면됨. CNT를 저장해서 CNTLIST에 DFS CNT를 ADD해줘야함.
        2-3: CNT ARRAYLIST를 SORT한 다음 출력
        출력방식:
        1. CNT ARRAYLSIT의 size 출력 후 엔터
        2.남은 요소들 전부 출력
       */
    }
}