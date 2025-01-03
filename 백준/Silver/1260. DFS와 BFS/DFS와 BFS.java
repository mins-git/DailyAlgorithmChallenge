

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    public static void DFS(int startNode, Map<Integer, List<Integer>> graph, boolean[] visited) {
        // 방문처리
        visited[startNode] = true;
        System.out.print(startNode + " ");

        // 현재 노드와 연결된 노드들을 순회
        List<Integer> neighbors = graph.getOrDefault(startNode, new ArrayList<>());

        // 정렬하여 순서 보장 (필요 시)
        Collections.sort(neighbors);

        for (int neighbor : neighbors) {
            if (!visited[neighbor]) {
                DFS(neighbor, graph, visited);
            }
        }
    }

    public static void BFS(int startNode, Map<Integer, List<Integer>> graph, boolean[] visited) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(startNode); // 시작 노드를 큐에 추가
        visited[startNode] = true;

        while (!queue.isEmpty()) {
            int currentNode = queue.poll(); // 큐에서 노드 꺼내기
            System.out.print(currentNode + " ");

            // 현재 노드와 연결된 모든 노드를 큐에 추가
            List<Integer> neighbors = graph.getOrDefault(currentNode, new ArrayList<>());
            Collections.sort(neighbors); // 정렬하여 탐색 순서 보장

            for (int neighbor : neighbors) {
                if (!visited[neighbor]) {
                    queue.offer(neighbor);
                    visited[neighbor] = true; // 방문 처리
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {

//        String input = "src/baekJoon/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputNMV = br.readLine().split(" ");

        int N = Integer.parseInt(inputNMV[0]); // 정점의 개수
        int M = Integer.parseInt(inputNMV[1]); // 간선의 개수
        int V = Integer.parseInt(inputNMV[2]); // 탐색을 시작할 정점의 번호

//        System.out.println("%d, %d, %d".formatted(N,M,V) );
//        System.out.printf("%d, %d, %d", N,M,V); // 이건 줄바꿈이 없음.

        // 그래프 초기화
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 1; i <=N; i++){
            graph.put(i, new ArrayList<>());
        }

//        System.out.println(graph);

        // 간선 정보 추가
        for (int x = 0; x <M; x++) {
            String[] edge = br.readLine().split(" ");
            int A = Integer.parseInt(edge[0]); // 시작 정점
            int B = Integer.parseInt(edge[1]); // 끝 정점

            graph.get(A).add(B);
            graph.get(B).add(A); // 무방향 그래프이므로 반대 방향도 추가
        }
//
//        for (int node: graph.keySet()){
//            System.out.println(node + ": " + graph.get(node));
//        }

        // 방문 여부 배열 초기화
        boolean[] visited = new boolean[N + 1];

        // DFS 실행
        boolean[] visitedForDFS = new boolean[N + 1]; // DFS 전용 방문 여부 배열
        DFS(V, graph, visitedForDFS);
        System.out.println();

        // BFS 실행
        boolean[] visitedForBFS = new boolean[N + 1]; // BFS 전용 방문 여부 배열
        BFS(V, graph, visitedForBFS);

    }
}