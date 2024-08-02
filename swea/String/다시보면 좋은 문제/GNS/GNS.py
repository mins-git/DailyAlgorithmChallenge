import sys

sys.stdin = open('input.txt')


def counting_sort(data, temp, k = 9):
    # data는 정렬해야할 배열
    # temp는 임시 저장값
    # k는 최대값이 될것임.
    counts = [0] * (k+1)

    # counts에 data의 실제값을 counts인덱스에 넣어줌으로써 숫자 세기.
    for i in range(0, len(data)):
        counts[data[i]] += 1

    # counts의 인덱스값을 더해줌
    # 더해줌으로써 너는 최소 4번째 위치에는 있겠네. 라고 알 수 있게됨.
    for i in range(1, k+1):
        counts[i] += counts[i-1]

    for i in range(len(temp) -1, -1, -1): # 실제로는 0까지 반복되겠네, 1개씩 감소하면서.
        counts[data[i]] -= 1
        temp[counts[data[i]]] = data[i]

    return temp

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):


    case, case_len = map(str, input().split())
    num_arr = list(map(str, input().split()))
    # num_arr_test = ['EGT', 'ONE', 'THR', 'SIX', 'ZRO', 'ZRO', 'NIN', 'FIV']
    find_arr = [['ZRO', 0],
        ['ONE', 1],
        ['TWO', 2],
        ['THR', 3],
        ['FOR', 4],
        ['FIV', 5],
        ['SIX', 6],
        ['SVN', 7],
        ['EGT', 8],
        ['NIN', 9]]

    result = []
    for i in num_arr :
        for j in range(10):
            if i == find_arr[j][0]:
                result.append(find_arr[j][1])

    result_count_arr = [0 for _ in range(len(num_arr))] # temp
    sort = counting_sort(result, result_count_arr, k=9)

    final_arr = []
    for i in sort:
        for j in range(10):
            if i == find_arr[j][1]:
                final_arr.append(find_arr[j][0])


    print(f'{case}')
    for i in range(len(final_arr)):
        print(final_arr[i], end=" ")

