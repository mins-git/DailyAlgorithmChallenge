import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt(); // 테스트 케이스 개수
        for (int i = 0; i < t; i++) {
            int x1 = sc.nextInt();
            int y1 = sc.nextInt();
            int r1 = sc.nextInt();
            int x2 = sc.nextInt();
            int y2 = sc.nextInt();
            int r2 = sc.nextInt();

            // 두 원의 중심 거리 구하기
            int dx = x2 - x1;
            int dy = y2 - y1;
            int distanceSquared = dx * dx + dy * dy;
            int radiusSum = (r1 + r2) * (r1 + r2);
            int radiusDiff = (r1 - r2) * (r1 - r2);

            // 교점의 개수 판별
            if (distanceSquared == 0 && r1 == r2) {
                System.out.println(-1); // 무한개 교점
            } else if (distanceSquared == radiusSum || distanceSquared == radiusDiff) {
                System.out.println(1); // 1개의 교점
            } else if (distanceSquared < radiusSum && distanceSquared > radiusDiff) {
                System.out.println(2); // 2개의 교점
            } else {
                System.out.println(0); // 교점 없음
            }
        }
    }
}
