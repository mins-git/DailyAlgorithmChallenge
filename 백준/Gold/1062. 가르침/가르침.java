
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.sql.Array;
import java.util.*;

import java.io.*;  // 입출력 관련 라이브러리 임포트
import java.util.*;  // 문자열 분리 및 집합 관련 라이브러리 임포트

public class Main {
    static int N, K;  // N: 단어의 수, K: 선택할 수 있는 문자 수
    static String[] words;  // 단어들을 저장할 배열
    static int maxReadableWords = 0;  // 읽을 수 있는 최대 단어 수 저장 변수

    public static void main(String[] args) throws IOException {
        // 입력을 위한 BufferedReader와 StringTokenizer 선언
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());  // 첫 번째 입력값은 단어의 개수 N
        K = Integer.parseInt(st.nextToken());  // 두 번째 입력값은 K (선택할 수 있는 문자 수)

        // 필수 문자 5개를 제외하고 K가 부족하면 바로 0 출력하고 종료
        if (K < 5) {
            System.out.println(0);  // K가 5 미만일 경우, 선택할 수 있는 문자가 부족하므로 0 출력
            return;
        }

        // 단어 입력받기
        words = new String[N];  // 단어를 저장할 배열 초기화
        for (int i = 0; i < N; i++) {
            words[i] = br.readLine();  // 각 단어를 배열에 저장
        }

        // 필수 문자 'a', 'n', 't', 'i', 'c'는 미리 방문 처리
        boolean[] visited = new boolean[26];  // 알파벳 26개에 대한 방문 여부를 나타내는 배열
        visited['a' - 'a'] = true;  // 'a' 문자 방문 처리
        visited['n' - 'a'] = true;  // 'n' 문자 방문 처리
        visited['t' - 'a'] = true;  // 't' 문자 방문 처리
        visited['i' - 'a'] = true;  // 'i' 문자 방문 처리
        visited['c' - 'a'] = true;  // 'c' 문자 방문 처리

        // 백트래킹 시작 (기본 5개 문자 제외한 나머지 문자 중에서 선택)
        backtracking(visited, 0, 0);  // 방문 배열과 함께 백트래킹을 시작

        System.out.println(maxReadableWords);  // 최대 읽을 수 있는 단어 수 출력
    }

    // 백트래킹 함수 (기본 5개 문자 제외한 나머지 문자들 중에서 선택)
    static void backtracking(boolean[] visited, int start, int count) {
        // K개의 문자를 모두 선택했으면 읽을 수 있는 단어 수 계산
        if (count == K - 5) {  // K-5 개의 문자를 추가로 선택했다면
            maxReadableWords = Math.max(maxReadableWords, countReadableWords(visited));  // 읽을 수 있는 단어 수 계산 후 최댓값 갱신
            return;  // 더 이상 선택할 필요 없으므로 종료
        }

        // 알파벳 a-z 중에서 아직 선택하지 않은 문자 선택
        for (int i = start; i < 26; i++) {
            if (!visited[i]) {  // 아직 선택하지 않은 문자라면
                visited[i] = true;  // 현재 문자를 선택 처리
                backtracking(visited, i + 1, count + 1);  // 백트래킹 재귀 호출 (다음 문자 선택)
                visited[i] = false;  // 백트래킹 후 현재 문자 선택을 취소
            }
        }
    }

    // 현재 선택된 문자들로 읽을 수 있는 단어 수 계산
    static int countReadableWords(boolean[] visited) {
        int readableWordsCount = 0;  // 읽을 수 있는 단어 수 초기화

        for (String word : words) {
            if (canRead(word, visited)) {  // 해당 단어를 읽을 수 있으면
                readableWordsCount++;  // 읽을 수 있는 단어 수 증가
            }
        }

        return readableWordsCount;  // 읽을 수 있는 단어 수 반환
    }

    // 특정 단어를 읽을 수 있는지 확인
    static boolean canRead(String word, boolean[] visited) {
        for (char c : word.toCharArray()) {  // 단어를 한 글자씩 확인
            // 아직 선택되지 않은 문자가 있으면 읽을 수 없음
            if (!visited[c - 'a']) {  // 해당 문자 방문 여부 확인
                return false;  // 읽을 수 없으면 false 반환
            }
        }
        return true;  // 모든 문자가 방문 처리되어 있으면 true 반환
    }
}


//
//public class Main {
//    static int maxCount = 0;
//
//    static void backtrack(ArrayList<ArrayList<String>> twoDimList, List<String> uniqueChars, boolean[] visited, int depth, int remaining, List<String> baseChars, List<String> currentSet) {
//        // remaining == 0: 더 이상 선택할 문자가 없다면 읽을 수 있는 단어 개수를 계산
//        if (remaining == 0) {
//            // 필수 알파벳들을 포함한 최종 문자 집합
//            List<String> finalSet = new ArrayList<>(baseChars);
//            finalSet.addAll(currentSet);
//
//            int count = countReadableWords(twoDimList, finalSet);
//            maxCount = Math.max(maxCount, count);
//            return;
//        }
//
//        for (int i = depth; i < uniqueChars.size(); i++) {
//            if (!visited[i]) {
//                visited[i] = true;
//                currentSet.add(uniqueChars.get(i));
//                backtrack(twoDimList, uniqueChars, visited, i + 1, remaining - 1, baseChars, currentSet);
//                currentSet.remove(currentSet.size() - 1);
//                visited[i] = false;
//            }
//        }
//    }
//
//
//    static int countReadableWords(ArrayList<ArrayList<String>> twoDimList, List<String> currentSet){
//        int count = 0;
//        for (ArrayList<String> word : twoDimList){
//            boolean readable = true;
//
//            // 단어의 각 문자가 currentSet에 포함되어 있는지 확인
//            for(String ch : word){
//                if(!currentSet.contains(ch)){
//                    readable = false;
//                    break;
//                }
//            }
//            if (readable) {
//                count ++;
//            }
//        }
//        return count;
//    }
//
//
//    public static void main(String[] args) throws IOException {
//
////        String input = "src/baekJoon/input.txt";
////        BufferedReader br = new BufferedReader(new FileReader(input));
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int[] NK = Arrays.stream(br.readLine().split(" "))
//                .mapToInt(Integer::parseInt)
//                .toArray();
//
//        int N = NK[0];
//        int K = NK[1];
//
//        ArrayList<ArrayList<String>> twoDimList = new ArrayList<>();
//
//        ArrayList<String> baseChars = new ArrayList<>(List.of("a", "n", "t", "i", "c"));
//
//        if (K < 5) {
//            System.out.println(0);
//            return;
//        }
//
//        // N개의 개수만큼 add하기
//        for (int i = 0; i < N; i++) {
//            twoDimList.add(new ArrayList<>());
//        }
//
//        for (int i = 0; i < N; i++) {
//            String preInput = br.readLine(); // 첫줄을 입력받은 후
//            for (char ch : preInput.toCharArray()) {
//                String str = String.valueOf(ch); // char > str 변환
//
//                if (!baseChars.contains(str)) {
//                    twoDimList.get(i).add(str);
//                }
//            }
//        }
//
//        // toDimList
//        Set<String> allchars = new HashSet<>();
//        for (ArrayList<String> list : twoDimList) {
//            allchars.addAll(list);
//        }
//        List<String> uniqueChars = new ArrayList<>(allchars);
//        boolean[] visited = new boolean[uniqueChars.size()];
//
//        // 백트래킹 메서드에 baseChars 전달
//        backtrack(twoDimList, uniqueChars, visited, 0, K - 5, baseChars, new ArrayList<>());
//
//        System.out.println(maxCount);
//    }
//}

/*
많은 단어를 읽을 수 있도록 하려고함.
K개의 글자를 가르칠 시간 밖에 없음.
K개의 글자만 읽을 수 있음.

남극언어의 모든 단어는 anta로 시작 tica로 끝남.
N개 밖에 없는 남극 언어.
학생들이 읽을 수 있는 단어의 최대값 구하는 프로그램 작성

N은 50보다 작거나 같은 자연수이고
K는 26보다 작거나 같은 자연수 또는 0임
길이가 8보다 크거나 같고 15보다 작거나 같음 모든 단어 중복 x


antic = 5개
5개 이하면 0 출력하면됨.

겹치는 숫자가 있는지 체크하면됨. 그러면?
2차원 리스트를 만들고, anta외에 추가로 필요한 char값을 배열에 add하고





1. 가장 많이 겹치는게 많은것?
1.1 char의 총 배열의 길이가 (K-5) 이상이면 continue진행(pass)
1.2 backtracking 사용. 재귀로 처음 인덱스 r을

[[r], [h, e, l, l, o], [r]]





 */