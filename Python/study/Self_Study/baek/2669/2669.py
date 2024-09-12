import sys

sys.stdin = open('input.txt')


# Testcase 수
T = 1
# Testcase 만큼 반복
for tc in range(1, T+1):




    #직사각형 네개의 합집합의 면적 구하기

    arr = [] # 겹치는 배열을 알기 위한 정리.
    for i in range(4):
        left_x, left_y, right_x, right_y = map(int, input().split())
        for y in range(right_y, left_y, -1):  # right y부터 left y까지 순회하기.
            for x in range(left_x, right_x, 1): #left_x부터 right_x까지 1씩증가
                arr.append([x,y])




    for_check_len = [tuple(x) for x in arr]
    print(len(set(for_check_len)))





