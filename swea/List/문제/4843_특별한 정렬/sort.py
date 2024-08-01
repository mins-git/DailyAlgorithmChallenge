import sys

sys.stdin = open('input.txt')


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):
    # 가장큰수, 가장 작은수, 2번째 큰수, 2번재 작은수 순으로 번갈아 정렬

    N = int(input()) # 정수의 개수

    def selecet(arr, k):
        for i in range(0, k):
            min_index = i
            for j in range(i+1, len(arr)):
                if arr[min_index] > arr[j]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr[k-1]


    print(f'#{tc} {}')
