import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class 음식물피하기{

    // 우 하 좌 상
    static int[] dr = {0,1,0,-1};
    static int[] dc = {1,0,-1,0};

    public static int bfs(int a, int b, int[][] bookdo, int N, int M){

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{a,b});

        bookdo[a][b] = 0;

        int cnt = 1; // 음식물 덩어리의 크기

        // 큐비면 종료
        while(!queue.isEmpty()){
            int [] curr = queue.poll();
            int r = curr[0];
            int c = curr[1];


            for (int d = 0; d < 4; d++){
                int nr = r + dr[d];
                int nc = c + dc[d];

                // N이 가로의 개수임. (세로의 길이)
                if(nr >= 0 && nr < N && nc >=0 && nc < M && bookdo[nr][nc] == 1){
                    bookdo[nr][nc] = 0;
                    queue.offer(new int[]{nr, nc}); // 정지조건
                    cnt ++;
                }
            }
        }

        return cnt;
    }

    public static void main(String[] args) throws IOException {

//        String input = "src/baekJoon/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String [] NMK = br.readLine().split(" ");

        int N = Integer.parseInt(NMK[0]); // 통로의 세로 길이
        int M = Integer.parseInt(NMK[1]); // 통로의 가로 길이
        int K = Integer.parseInt(NMK[2]); // 음식물 쓰레기의 개수

        // 이차원 배열로 복도 구성
        int [][] bookdo = new int [N][M];

        for (int i = 0; i < K; i++){
            String[] parts = br.readLine().split(" ");
            int x = Integer.parseInt(parts[0]);
            int y = Integer.parseInt(parts[1]);
            bookdo[x-1][y-1] = 1;
        }

//        System.out.println(Arrays.deepToString(bookdo));
        int result = 0 ;

        for (int a = 0; a < N; a++){
            for (int b = 0; b < M; b++){
                if(bookdo[a][b] == 1){
                    int cnt = bfs(a, b, bookdo, N, M );
                    result = Math.max(result, cnt);
                } else continue;
            }
        }

        System.out.println(result);


    /*
    음식물 피하기
    3끼의 식사를 해결하는 공간.
    제일 큰 음식물만 피해가려고함.




    */

    }
}