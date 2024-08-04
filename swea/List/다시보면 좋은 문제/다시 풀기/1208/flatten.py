import sys
sys.stdin = open('input.txt')


# 평탄화 작업을 진행할것임.

# 가장 높은곳에잇는것을 낮은곳으로 이동하는과정이 있을것임.
# 정렬 후
# 1번째의것을 제일 마지막에 넣어주면 되겠네.
# dump 이후
#
# 최고점 - 최저점
for tc in range(1):




    # # 버블정렬
    #
    # arr_len = len(arr)
    #
    # def bubble(arr):
    #     n = len(arr)
    #     for i in range(n):
    #         swap = False
    #         for j in range(n - 1 - i):
    #             if arr[j] > arr[j+1]:
    #                 arr[j], arr[j+1] = arr[j+1], arr[j] # 파이썬 편함,,, 이게 돼?
    #                 swap = True
    #         if not swap:
    #             break
    #
    # bubble(arr) # 정렬됨.
    #
    # # 제일 오른쪽에 있는걸 1번재로 더해주는과정임. 이걸 반복
    #
    # # 덤프가 0보다 클동안 반복해줘
    # while dump > 0 :
    #
    #     arr[-1] -= 1
    #     arr[0] += 1
    #     dump -= 1
    #     bubble(arr)
    #
    #
    # bubble(arr)
    # print(f'{arr[-1] - arr[0]}')

    dump = int(input())
    arr = list(map(int,input().split()))

    # 카운팅정렬

    arr_max = max(arr)
    temp = [0] * len(arr)

    def counting_sort(data, temp, k= arr_max):
        # data는 정렬해야할 배열
        # temp는 임시 저장값
        # k는 최대값이 될것임.
        counts = [0] * (k + 1)

        # counts에 data의 실제값을 counts인덱스에 넣어줌으로써 숫자 세기.
        for i in range(0, len(data)):
            counts[data[i]] += 1

        # counts의 인덱스값을 더해줌
        # 더해줌으로써 너는 최소 4번째 위치에는 있겠네. 라고 알 수 있게됨.
        # 예를들어 counts = [0, 1, 2, 2, 1, 0, 0, 0, 1] 이런배열이
        # counts = [0, 1, 3, 5, 6, 6, 6, 6, 7] 이렇게 바뀌게됨.
        for i in range(1, k + 1):
            counts[i] += counts[i - 1]
        sorted_arr = [0] * len(data)
        for i in range(len(data) - 1, -1, -1):  # 실제로는 0까지 반복되겠네, 1개씩 감소하면서.
            counts[data[i]] -= 1
            sorted_arr[counts[data[i]]] = data[i]

        return sorted_arr


    # 덤프가 0보다 클동안 반복해줘
    while dump > 0 :

        arr[-1] -= 1
        arr[0] += 1
        dump -= 1
        arr = counting_sort(arr, arr_max)


    print(f'{arr[-1] - arr[0]}')




