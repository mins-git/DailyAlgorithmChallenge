package baekJoon;


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main{
    public static void main(String[] args) throws IOException {

        String input = "src/baekJoon/input.txt";
        BufferedReader br = new BufferedReader(new FileReader(input));

        int coumputerCnt = Integer.parseInt(br.readLine());
        int connenctCnt =  Integer.parseInt(br.readLine());

        // 연결된 노드 작성



        /*
        바이러스
        한 컴퓨터가 바이러스에 걸리면 웜 바이러스는 네트워크를 통해 전파됨.
        컴퓨터와 네트워크 상에 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸림
        즉 BFS

        1번으로 시작해서 바이러스 걸리는 컴퓨터 수 출력



         */

    }
}