import sys

sys.stdin = open('input.txt')


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    # for문을 돌면서, 최대값 최소값 체크한 후 빼주면됨.
    # 중간에 최대 - 최소가 1보다 작거나 같을경우는 멈춰.

    dump = int(input())
    data = list(map(int, input().split()))
    count = 0
    # 덤프만큼 순회
    while count < dump:

        # 앞뒤 데이터 비교하여 max와 min 구하기.
        # for x in range(len(data)):
        max_index = 0
        min_index = 0

        for i in range(1, len(data)):
            if data[i] > data[max_index]:
                max_index = i
            if data[i] < data[min_index]:
                min_index = i

        # data의 maxindex부분을 더해주고 나머지는 빼주기.

        max_index = data.index(max(data))
        min_index = data.index(min(data))
        if data[max_index] - data[min_index] <= 1 :
            break

        data[max_index] -= 1
        data[min_index] += 1
        count +=1

    max_index = 0
    min_index = 0

    for i in range(1, len(data)):
        if data[i] > data[max_index]:
            max_index = i
        if data[i] < data[min_index]:
            min_index = i

    result = data[max_index] - data[min_index]

    print(f'#{tc} {result}')

