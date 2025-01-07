package baekJoon;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main{

    public static int dfs(int r, int c, int[][] maze, HashMap<String, Boolean> visited, int N, int M, int[] dr, int[] dc, int depth){


        // 방문처리
        if (r == N -1  && c == M -1){
            return depth;
        }

        String key = r + "," + c;
        if (visited.containsKey(key) && visited.get(key)){
            return Integer.MAX_VALUE;
        }
        visited.put(key, true);

        int minDepth = Integer.MAX_VALUE;

        for (int d = 0; d < 4; d++){
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr >= 0 && nr < N && nc >=0 && nc < M && maze[nr][nc] != 0){
                int cnt = dfs(nr, nc, maze, visited,N, M, dr, dc,depth+1);
                minDepth = Math.min(minDepth, cnt);
            }
        }

        visited.put(key, false);

        return minDepth;
    }

    public static void main(String[] args) throws IOException {

//        String input = "src/baekJoon/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String [] NM = br.readLine().split(" ");

        int N = Integer.parseInt(NM[0]);
        int M = Integer.parseInt(NM[1]);

        //가로(행) 세로(열)로 초기화
        int[][] maze = new int[N][M];

        for (int i = 0; i < N; i++){
            char[] line = br.readLine().toCharArray();
            for(int j = 0; j< M; j++){
                // 아스키코드 48만큼 제거해주면됨.
                maze[i][j] = line[j] - '0';
            }
        }

        // deepToString을 사용하면 내부 내용까지 가지고 갈 수 있음.
//        System.out.println(Arrays.deepToString(maze));

        // 방문처리할 배열 선택 not in으로 체크하면됨.
        HashMap<String, Boolean> visited = new HashMap<String, Boolean>();

        // 오아왼위 델타
        int[] dr = {0, 1, 0,-1};
        int[] dc = {1, 0, -1,0};

        int r = 0;
        int c = 0;

        int result = dfs(r, c, maze, visited, N, M, dr, dc, 1);

        System.out.println(result);




        /*
        N*M 배열의 미로가 있음.

        1은 이동 할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타냄
        이러한 미로가 존재할때 에,

        (1,1) -> 출발해서 (N,M)으로 도착하는 최소의 칸 수를 구하는 프로그램 작성.

        상화좌우로만 이동 가능

        최소칸 출력
        0번째 인덱스에서 출발 후 - > (N-1 번째 인덱스, M-1 번째인덱스)까지 도착가능하게 설정

        깊이우선탐색 dfs하면될것같고,
        도착할 수 없으면 0 출력해봐.
        (N-1,M-1) 인덱스 도착시에 break하는 백트레킹을 사용하면됨.




         */
    }
}


// 효율적인 코드는 아래와 같음.

//public class Main {
//
//    // 방향: 우, 하, 좌, 상
//    static int[] dr = {0, 1, 0, -1};
//    static int[] dc = {1, 0, -1, 0};
//
//    public static void main(String[] args) throws IOException {
//        String input = "src/baekJoon/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
//
//        String[] NM = br.readLine().split(" ");
//        int N = Integer.parseInt(NM[0]);
//        int M = Integer.parseInt(NM[1]);
//
//        // 미로 배열 초기화
//        int[][] maze = new int[N][M];
//        for (int i = 0; i < N; i++) {
//            char[] line = br.readLine().toCharArray();
//            for (int j = 0; j < M; j++) {
//                maze[i][j] = line[j] - '0'; // '0'을 빼서 0과 1로 변환
//            }
//        }
//
//        // BFS를 위한 큐 초기화
//        Queue<int[]> queue = new LinkedList<>();
//        queue.offer(new int[]{0, 0}); // 출발점 (0, 0)
//
//        // 방문 처리 배열
//        boolean[][] visited = new boolean[N][M];
//        visited[0][0] = true;
//
//        // BFS 시작
//        while (!queue.isEmpty()) {
//            int[] curr = queue.poll();
//            int r = curr[0];
//            int c = curr[1];
//
//            // 목적지에 도달하면 결과 출력
//            if (r == N - 1 && c == M - 1) {
//                System.out.println(maze[r][c]);
//                return;
//            }
//
//            // 4방향 탐색
//            for (int d = 0; d < 4; d++) {
//                int nr = r + dr[d];
//                int nc = c + dc[d];
//
//                // 미로 범위 내에 있고, 이동할 수 있는 곳인 경우
//                if (nr >= 0 && nr < N && nc >= 0 && nc < M && maze[nr][nc] == 1 && !visited[nr][nc]) {
//                    visited[nr][nc] = true;
//                    maze[nr][nc] = maze[r][c] + 1; // 이전 칸에서 1을 더하여 거리를 기록
//                    queue.offer(new int[]{nr, nc});
//                }
//            }
//        }
//
//        // 도달 불가능한 경우 (보통 여기까지 오지 않음)
//        System.out.println(0);
//    }
//}
