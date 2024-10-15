package algorithms.Java_Skill_Boost_Challenge.직사각형_네개의_합집합의_면적_구하기_2669;

//import java.io.FileReader;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

//import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {



//        String filePath = "src/algorithms/Java_Skill_Boost_Challenge/직사각형_네개의_합집합의_면적_구하기_2669/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(filePath));

        boolean[][] grid = new boolean[101][101]; // bool 타입으로 101개의 행렬 생성
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 사각형 정보를 입력받아 grid에 표시
        for (int i = 0; i < 4; i++){
            String[] input = br.readLine().split(" ");
            int x1 = Integer.parseInt(input[0]);
            int y1 = Integer.parseInt(input[1]);
            int x2 = Integer.parseInt(input[2]);
            int y2 = Integer.parseInt(input[3]);


            for(int x = x1; x < x2; x++){
                for(int y= y1; y < y2; y++){
                    grid[x][y] = true;
                }
            }

        }

        // 겹치는 영역의 넓이 계산
        int area = 0;
        for(int x = 0; x<=100; x++){
            for(int y=0; y<=100; y++){
                if(grid[x][y]){
                    area++; // true인 경우 넓이 증가.
                }
            }
        }
        System.out.println(area);







//        String filePath = "src/algorithms/Java_Skill_Boost_Challenge/직사각형_네개의_합집합의_면적_구하기_2669/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(filePath));

//          백준 진행시 아래 사용.
////        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//
////        문자열 입력시
////        String str = "";
////        str = br.readLine();
//
////         String str = br.readline();
////
////        숫자 입력시
////        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
////        int number = Integer(parseInt(br.readline()));
//
//        String line; // 파일에서 읽은 각 줄을 저장할 변수 선언
//        while ((line = br.readLine()) != null) { // 파일이 끝까지 도달할때까지 진행.
//            // 공백을 기준으로 분리하여 배열에 저장
//            String[] values = line.split(" "); // [1, 2, 4, 4]
////            System.out.println(Arrays.toString(values)); // [1, 2, 4, 4]
//            // 정수 배열로 변환
//            int[] numbers = new int[values.length];
//            for (int i = 0; i < values.length; i++) {
//                numbers[i] = Integer.parseInt(values[i]);
//            }
//
//            // 읽어온 정수 배열 출력 (예시)
//            System.out.println("읽은 정수: " + numbers[0] + ", " + numbers[1] + ", " + numbers[2] + ", " + numbers[3]);
//        }

    }
}
