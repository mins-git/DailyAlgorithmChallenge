import sys

sys.stdin = open('input.txt')


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    print(T) # 테스트 케이스 갯수 잘 들어오는지 확인
    # 입력을 리스트로 변환
    # print(list(map(int, input().split()))) # input 함수는 파일 한 줄씩 문자열 형태로 받아옴.
    # a, b, c, d = map(int,input().split())
    # print(a,c,b,d)

    # 그냥 문자열이 들어올때에는, input()만하면됨. 굳이 split, map 해줄 필요없음.

    arr = list(map(int,input().split()))

    print(arr) # [5, 6, 1, 2] 이렇게 print하면서 진행 해보기.

    