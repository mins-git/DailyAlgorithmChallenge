import sys

sys.stdin = open('input.txt')


# 행, 열, 대각선 2개 각 줄의 합중 쵀댓값 리턴

# Testcase 수
T = 10
# Testcase 만큼 반복
for tc in range(1, T+1):

    def put_result(sumresult, result):
        if sumresult > result:
            result = sumresult

        return result

    # board = [[int(x) for x in range(100) input()] for _ in range(100)]
    test_case = int(input())
    # 행이 들어옴.
    board = []
    result = 0
    sumresult = 0



    # 100 배열 변수 안에 넣기
    for index in range(100):
        # 행 입력받고 2차원 배열로 만들기
        row = input().split()
        board.append([int(x) for x in row])

    sumresult = 0
    # 우측 아래 대각선
    for i in range(100):
        for j in range(100):
            if i == j :
                sumresult += board[i][j]

    result = put_result(sumresult, result)

    sumresult = 0
    # 좌측 아래 대각선
    for i in range(100):
        for j in range(100):
            if 100 - i == j :
                sumresult += board[i][j]

    result = put_result(sumresult, result)

    # 행 덧셈(가로)
    for i in range(100):
        sumresult = 0
        for j in range(100):
            sumresult += board[i][j]
        result = put_result(sumresult, result)


    # 열 덧셈
    for i in range(100):
        sumresult = 0
        for j in range(100):
            sumresult += board[j][i]
        result = put_result(sumresult, result)



    print(f'#{tc} {result}')
