import sys

sys.stdin = open('input.txt')


def binarySearch(N, key):
    start = 0
    end = N - 1
    count = 0
    while start <= end:
        middle = (start + end) // 2
        if middle == key:
            return count
        elif middle > key:
            end = middle - 1
            count += 1
        else :
            start = middle + 1
            count += 1
    return count

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    P, Pa, Pb = map(int, input().split())    # 전체 쪽 수, pa. pb 주어짐


    if binarySearch(P, Pa)+1 > binarySearch(P, Pb):
        print(f'#{tc} A')
    elif binarySearch(P, Pa)+1 < binarySearch(P, Pb):
        print(f'#{tc} B')
    else : print(f'#{tc} 0')







## 이진 탐색 게임 진행
# 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이김.

# 400쪽 왼쪽 1 오른쪽 400 중간이 CTIN(L_R/2

# 비긴경우 0 누가 이겼나 체크


