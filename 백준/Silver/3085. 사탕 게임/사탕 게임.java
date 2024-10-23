import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void swap(char[][] candyList, int x1, int y1, int x2, int y2) {
        char temp = candyList[x1][y1];
        candyList[x1][y1] = candyList[x2][y2];
        candyList[x2][y2] = temp;
    }

    public static int checkMaxCandies(char[][] candyList, int N) {
        int maxCount = 1;

        // 행을 기준으로 연속된 사탕 확인
        for (int i = 0; i < N; i++) {
            int count = 1;
            for (int j = 1; j < N; j++) {
                if (candyList[i][j] == candyList[i][j - 1]) {
                    count++;
                } else {
                    maxCount = Math.max(maxCount, count);
                    count = 1;
                }
            }
            maxCount = Math.max(maxCount, count);
        }

        // 열을 기준으로 연속된 사탕 확인
        for (int j = 0; j < N; j++) {
            int count = 1;
            for (int i = 1; i < N; i++) {
                if (candyList[i][j] == candyList[i - 1][j]) {
                    count++;
                } else {
                    maxCount = Math.max(maxCount, count);
                    count = 1;
                }
            }
            maxCount = Math.max(maxCount, count);
        }

        return maxCount;
    }

    public static void main(String[] args) throws IOException {

//        String file = "src/baekJoon/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(file));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        char[][] candyList = new char[N][N];

        for (int z = 0; z < N; z++) {
            candyList[z] = br.readLine().toCharArray();
        }
//        System.out.println(candyList); //

        int maxCandy = 0;

        // 빨 C 파 P 초 Z 노 Y
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {

                // 오른쪽 사탕이랑 교환
                if (j + 1 < N) {
                    swap(candyList, i, j, i, j + 1);
                    maxCandy = Math.max(maxCandy, checkMaxCandies(candyList, N));
                    swap(candyList, i, j, i, j + 1); // 원상 복구
                }

                if (i + 1 < N){
                    swap(candyList, i, j , i+1, j);
                    maxCandy = Math.max(maxCandy, checkMaxCandies(candyList,N));
                    swap(candyList,i,j,i+1,j);
                }

            }

        }
        System.out.println(maxCandy);
    }
}