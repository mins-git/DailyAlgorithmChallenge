import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.*;

public class Main{

    public static int bfs(Map<Integer, List<Integer>> graph, int start) {
        Set<Integer> visited = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited.add(start);

        int count = 0;

        while (!queue.isEmpty()) {
            int current = queue.poll();
            count++;

            for (int neighbor : graph.getOrDefault(current, Collections.emptyList())) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.add(neighbor);
                }
            }
        }
        return count;
    }
    public static void main(String[] args) throws IOException {

//        String input = "src/baekJoon/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int coumputerCnt = Integer.parseInt(br.readLine());
        int connenctCnt =  Integer.parseInt(br.readLine());

        // 연결된 노드 작성
        int [][] node = new int [connenctCnt][2];

        for (int i = 0; i < connenctCnt; i++){
            String [] inputA = br.readLine().split(" ");
            int a = Integer.parseInt(inputA[0]);
            int b = Integer.parseInt(inputA[1]);
            node[i][0] = a;
            node[i][1] = b;
        }

        // 인접 리스트 표현
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] edge : node) {
            graph.putIfAbsent(edge[0], new ArrayList<>());
            graph.putIfAbsent(edge[1], new ArrayList<>());
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]); // 무향 그래프
        }


        int startNode = 1;
        int count = bfs(graph, startNode);

        System.out.println(count-1);

    }
}