
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main{
    static int[][] delt = {
            {0, 1},   // 오른쪽 (가로 +1)
            {1, 0},   // 아래 (세로 +1)
            {0, -1},  // 왼쪽 (가로 -1)
            {-1, 0}   // 위 (세로 -1)
    };


    public static int DFS(int j, int o, ArrayList<ArrayList<String>> mapList, boolean[][] visited, boolean mySold ){

        visited[j][o] = true;

        int power = 1; // 현재 병사의 시작은 1

        // 네 방향으로 탐색
        for(int i = 0; i< 4; i++){
            int nj = j + delt[i][0];
            int no = o + delt[i][1];

            if(nj >= 0 && nj < mapList.size() && no >= 0 && no < mapList.get(0).size()){

                // 방문하지 않았고, 같은 팀 병사라면 DFS 진행
                if (!visited[nj][no] && mapList.get(nj).get(no).equals(mySold ? "W" : "B")) {
                    power += DFS(nj, no, mapList, visited, mySold); // 연결된 병사 수를 더함
                }
            }
        }
        return power;
    }

    public static void main(String[] args) throws IOException {
//      String input = "src/baekJoon/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String [] inputX = br.readLine().split(" ");

        int N = Integer.parseInt(inputX[0]); // 가로
        int M = Integer.parseInt(inputX[1]); // 세로

        ArrayList<ArrayList<String>> mapList = new ArrayList<>();

        for(int i = 0; i < M; i++){
            ArrayList<String> row = new ArrayList<>();
            String[] line = br.readLine().split(""); // 입력을 한 글자씩 분리

            for (String ch : line) {
                row.add(ch); // 분리된 글자를 row에 추가
            }
            mapList.add(row); // 한 줄을 mapList에 추가
        }

//        System.out.println(mapList);


        // 방문 처리할 2차원 배열
        boolean[][] visited = new boolean[M][N];
        int totalWPower = 0;
        int totalBPower = 0;

        // 가로 체크
        for (int o = 0; o < N; o ++){
            // 세로 체크
            for(int j = 0; j < M; j++){
                if(!visited[j][o]){

                    // 흰옷과  파란옷에 따라 dfs 진행
                    if (mapList.get(j).get(o).equals("W")){
                        totalWPower += Math.pow(DFS(j, o, mapList, visited, true), 2); // 흰옷 병사의 위력 제곱 합
                    } else {
                        totalBPower += Math.pow(DFS(j, o, mapList, visited, false), 2); // 파란옷 병사의 위력 제곱 합
                    }
                }
            }
        }

        System.out.println(totalWPower + " " + totalBPower);

    }
}