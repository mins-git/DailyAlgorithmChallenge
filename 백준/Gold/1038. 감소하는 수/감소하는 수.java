import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

// 1038 감소하는 수
public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        // 감소하는 수를 저장할 리스트
        List<Long> decreasingNumbers = new ArrayList<>();

        // 0부터 9까지의 한 자리 숫자 먼저 추가
        for (long i = 0; i < 10; i++) {
            decreasingNumbers.add(i);
        }

        // 감소하는 수 생성
        for (int i = 0; i < decreasingNumbers.size(); i++) {
            long current = decreasingNumbers.get(i);

            // 마지막 숫자 추출
            long lastDigit = current % 10;

            // 마지막 숫자보다 작은 숫자들로 새로운 감소하는 수 생성
            for (long j = 0; j < lastDigit; j++) {
                long newNum = current * 10 + j;
                decreasingNumbers.add(newNum);
            }
        }

        // N번째 감소하는 수 출력 (0부터 시작)
        System.out.println(N < decreasingNumbers.size() ? decreasingNumbers.get(N) : -1);
    }
}


////1038 감소하는 수
//public class Main{
//
//    static int N;
//    static int cnt = 0;
//    static long result = -1;
//
//
//    public static void backtrack(long num) {
//        // 현재 숫자를 결과 후보로 추가
//        cnt++;
//
//        // N번째 감소하는 수를 찾으면 결과 저장
//        if (cnt == N) {
//            result = num;
//            return;
//        }
//
//        // 마지막 자릿수 추출
//        long lastDigit = num % 10;
//
//        // 마지막 숫자보다 작은 숫자들로 새로운 감소하는 수 생성
//        for (long i = 0; i < lastDigit; i++) {
//            long newNum = num * 10 + i;
//            backtrack(newNum);
//        }
//    }
//
//    public static void main(String[] args) throws IOException {
//
//        String input = "src/baekJoon/input.txt";
//        BufferedReader br = new BufferedReader(new FileReader(input));
////        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        N = Integer.parseInt(br.readLine());
//
//
//        // 한 자리 숫자인 경우 바로 처리
//        if( N < 10 ){
//            result = N;
//            System.out.println(result);
//            return;
//        }
//
//        // 백트래킹 시작(0부터 9까지 탐색)
//        for (int i =0; i <=9; i++){
//            backtrack(i);
//        }
//
//        System.out.println(result);
//
//    }
//}

/*
음이 아닌 정수 X의 가장 큰 자릿수부터 작은 자리수까지 감소한다면
그 수를 감소하는 수라고 한다.
ex) 54321, 321, 950

감소하는 수가 아닌수:
ex) 322 958

N번째로 감소하는 수를 출력하는 프로그램을 만드시오.


예외사항:
1. 0은 0번째 감소하는 수.
2. 1은 1번째 감소하는 수 임.
3. N번째 감소하는 수가 없다면 -1을 출력하면됨.


예시:
18 입력시 42출력됨.

0 = 0 번째 감소하는 수를 제외하고,

1, 2, 3,4,5,6,7,8,9 = 1번째 감소하는 수 라고하면
10
20 21
30 31 32
40 41 42 = > 이런식으로 몇번재 감소하는 수가 있는지 체크하면됨.
n이 1000000보다 작거난 같은 수

방법 1.
1. 카운트를 세기 위한 CNT 변수 선언 및 1로 초기화 만들기.
1-1 CNT와 N이 같아지는 순간 종료 WHILE문 써도될듯?
2. 감소하는 수인지 체크해야됨 (체크하는법)
2-1 RECENT NUM변수 만들기
2-2 RECNET NUM를 1부터 +1 진행. (여기에 예외 문구 추가 n의값과 같으면 break)
2-3 만약 RECENT NUM가 10보다 작으면 (10 > RECNET NUM)
    2-3.1 : +1씩 진행하면서 CNT + 해주고 RECENT NUM도 +1 해주면됨.

2-4 RECENT NUM이 10보다 클경우
    2-4.1 : 10보다 클 경우, 숫자를 분리한 후 LIST에 담기
            예를들어 321이면 [3,2,1]로 담기
    2-4.2 : 인덱스를 기준으로 FOR문을 돌려 앞의 인덱스보다 뒤에 인덱스 값의 값이 작으면
    CNT +1 후 RECENT NUM +1
    2-4.2 : 앞의 인덱스보다 뒤에 인덱스가 더 크면 앞의 인덱스의 값을 +1해주고 뒤의 인덱스값을 0 으로 바꿔준 후
            [3,3,0]과 같은값을 330 INT 값으로 변환해주기.
            변환된 값을 recent num에 재 할당.

방법 2 백트래킹 활용
1. 카운트를 세기 위한 cnt 변수 선언 및 0로 초기화
2. recent num을 선언 및 0으로 초기화
3. backtarck 함수 작성
3.1: 정답 조건처리:
    if (cnt와 N이 같다면){정답처리하면됨.} return

3.2: 불가능한 조건 가지치기 (예외처리)
    if (recentNum이 10보다 작을경우){
    cnt는 1을 높여주고, 탈출해
    recnetNum 1높여주고 탈출해
    } return

3.2: 가능한 선택지:
    for(int i = 0; ){

    }


 */

//        System.out.println( ((Object) N).getClass().getName() ); // java.lang.Integer




//    static void backtrack(long num){
//        // 종료조건(기저조건) 감소하는 수를 찾았으면 종료
//        if( cnt ==N ) return;
//
//        // 예외조건
//        cnt++;
//        if (cnt == N) {
//            result = num;
//            return;
//        }
//
//        // 다음 자릿수 탐색(num의 마지막 자릿수보다 작은 숫자만 선택 가능)
//        for (int i = 0; i < num % 10; i++) {
//            backtrack(num * 10 + i);
//        }
//
//    }
