import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int computerCnt = Integer.parseInt(br.readLine());
        int connectionCnt = Integer.parseInt(br.readLine());

        List<Integer>[] network = new ArrayList[computerCnt + 1];
        for (int i = 1; i <= computerCnt; i++) {
            network[i] = new ArrayList<>();
        }

        for (int i = 0; i < connectionCnt; i++) {
            String[] connection = br.readLine().split(" ");
            int a = Integer.parseInt(connection[0]);
            int b = Integer.parseInt(connection[1]);
            network[a].add(b);
            network[b].add(a);
        }

        System.out.println(countInfectedComputers(network));
    }

    private static int countInfectedComputers(List<Integer>[] network) {
        boolean[] visited = new boolean[network.length];
        Stack<Integer> stack = new Stack<>();
        int infectedCount = 0;

        stack.push(1);
        visited[1] = true;

        while (!stack.isEmpty()) {
            int current = stack.pop();
            for (int neighbor : network[current]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    stack.push(neighbor);
                    infectedCount++;
                }
            }
        }

        return infectedCount;
    }
}
