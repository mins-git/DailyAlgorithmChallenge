import sys
sys.stdin = open('input.txt')


def check_bingo(N,matrix):
    # 가로체크, 세로체크. 대각선, 반대대각선 체크
    bingo_count = 0

    # 가로체크
    for i in range(5):
        if sum(matrix[i]) == 5:
            bingo_count += 1

    #세로체크
    for i in range(5):
        # sum(row[i] for row in matrix) 부분을 사용하여 열의 합을 계산
        # transpose를 사용하지 않고 바로 세로줄을 확인
        if sum(row[i] for row in matrix) == 5:
            bingo_count += 1


    # 대각선 체크 (변경됨)
    # 각 대각선의 원소를 직접 합산하여 확인
    if sum(matrix[i][i] for i in range(5)) == 5:  # 주요 대각선 확인
        bingo_count += 1
    if sum(matrix[i][N - i] for i in range(5)) == 5:  # 반대 대각선 확인
        bingo_count += 1
    return bingo_count


def bingo(chul,sahwe):

    # matrix 초기화를 bingo 함수 내에서 수행
    matrix = [[0] * 5 for _ in range(5)]

    # sahew의 인덱스를 순회하면서
    for i in range(len(sahwe)):
        num = sahwe[i]
        for r in range(5):
            for c in range(5):
                # 가로체크, 세로체크, 대각선, 반대 대각선체크
                if num == chul[r][c]:  # 만약 5를 외치면
                    matrix[r][c] = 1  # 5를 1로바꿔줘.

                    if check_bingo(5, matrix) >= 3:
                        return i + 1
    return -1


chul = [list(map(int, input().split())) for _ in range(5)]
sahwe = []
for _ in range(5):
    sahwe.extend(map(int, input().split()))

# 빈배열 만들기
print(bingo(chul,sahwe))