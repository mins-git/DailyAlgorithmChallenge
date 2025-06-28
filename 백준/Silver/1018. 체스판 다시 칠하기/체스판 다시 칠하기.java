import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static char WHITE = 'W';
    static char BLACK = 'B';

    public static int checkBoard(char[][] board, int startRow, int startCol){
        int repaintCount1 = 0;
        int repaintCount2 = 0;

        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                char expectedColor1 = ((i + j) % 2 == 0) ? WHITE : BLACK;
                char expectedColor2 = ((i + j) % 2 == 0) ? BLACK : WHITE;

                if (board[startRow + i][startCol + j] != expectedColor1) repaintCount1++;
                if (board[startRow + i][startCol + j] != expectedColor2) repaintCount2++;
            }
        }
        return Math.min(repaintCount1, repaintCount2);
    }


    public static void main(String[] args) throws IOException {

        String input = "src/input.txt";

//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String [] inputStr = br.readLine().split(" ");
        int M = Integer.parseInt(inputStr[0]);
        int N = Integer.parseInt(inputStr[1]);

        char[][] board = new char[M][N];
        for (int i = 0; i < M ; i++){
            board[i] = br.readLine().toCharArray();
        }

        int min = Integer.MAX_VALUE;

        for(int i = 0; i <= M - 8; i ++){
            for (int j = 0; j <= N -8; j++){
                int repaint = checkBoard(board, i, j);
                if (repaint < min){
                    min = repaint;
                }
            }
        }

        System.out.println(min);

        


        /*
        MxN 보드 88 크기의 체스로 만들려고함.
        지민이가 다시 칠해야되는 정사각형의 최소 개수를 구하는 프로그램?

         */

    }
}
