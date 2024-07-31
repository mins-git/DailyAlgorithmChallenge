import sys

sys.stdin = open('input.txt')


# 실제로 10개의 정수를 입력 받을 때에, 부분집합의 합이 0이되는 것이 존재하는지
# 존재하면 1 false면 0 출력


# 부분 집합 구하기

T = int(input())

for tc in range(1, T+1):

    Data = list(map(int, input().split()))
    Data_len = len(Data)
    found_zero = False

    for i in range(1 << Data_len):
        sum_data = 0

        for j in range(Data_len):
            if i & (1 << j):
                sum_data += Data[j]

        if sum_data == 0 and i !=0 :
            found_zero = True
            break

    if found_zero :
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')