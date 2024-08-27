import sys
sys.stdin = open('input.txt')


"""
왼쪽 꼭지점 좌표 xy랑 위꼭지점 좌표  pq주어짐

직사각형이 겹치면 a
선분이 겹치면 b
점이 겹치면 c
공통부분이 없으면 d 출력.
"""



for tc in range(1, 5):
    fir_x, fir_y,fir_x2, fir_y2, sec_x, sec_y, sec_x2, sec_y2 = map(int, input().split())

    """
    x의 사이값이고, y의 사이값이면 a
    x의 선 y선 4선과 같은라인선이면 b
    1개면 c
    없으면 d
    """
    if fir_x2 < sec_x or sec_x2 < fir_x or fir_y2 < sec_y or sec_y2 < fir_y:
        print('d')

    elif (fir_x == sec_x2 and fir_y == sec_y2) or (fir_x2 == sec_x and fir_y == sec_y2) or \
            (fir_x == sec_x2 and fir_y2 == sec_y) or (fir_x2 == sec_x and fir_y2 == sec_y) :
        print('c')
    elif fir_x2 == sec_x or fir_x == sec_x2 or fir_y2 == sec_y or fir_y == sec_y2:
        print('b')

    else: print('a')




# --------------------------------------------------------
# 메모리 초과
    # # first
    # for i in range(fir_x, fir_x2+1):
    #     for j in range(fir_y, fir_y2+1):
    #         first_arr.append([i,j])
    #
    # # sec
    # for i in range(sec_x, sec_x2+1):
    #     for j in range(sec_y, sec_y2+1):
    #         second_arr.append([i,j])
    #
    #
    # # 중간에 겹치는부분?
    # for i in first_arr:
    #     for j in second_arr:
    #         if i == j :
    #             count_arr.append([i])
    #
    #
    # # 하나라도 겹치는게 없으면 공통없는 d, 점이 겹치면 c
    # if len(count_arr) == 0:
    #     print('d')
    # elif len(count_arr) == 1:
    #     print('c')
    # elif len(count_arr) > 1:
    #     # 여기는 직사각형이나, 선분일것임.

# ---------------------------------------------------
# 틀림
        # 좌측 상단 이 첫번째 안에있거나, 우측상단 안에잇거나, 좌측하단 안에, 우측하단안에 있으면
    # first가 더 크다는 가정
    # if (fir_x <= sec_x <= fir_x2 and fir_y <= sec_y2 <= fir_y2) or (fir_x <= sec_x2 <= fir_x2 and fir_y <= sec_y2 <= fir_y2) or \
    #     (fir_x <= sec_x <= fir_x2 and fir_y <= sec_y <= fir_y2) or (fir_x <= sec_x <= fir_x2 and fir_y <= sec_y <= fir_y2):
    #     print('a')
    # # sec가 더 크다는 가정
    # elif (fir_x <= sec_x <= fir_x2 and sec_y <= fir_y2 <= sec_y2) or (fir_x <= sec_x2 <= fir_x2 and sec_y <= fir_y2 <= sec_y2) or \
    #     (fir_x <= sec_x <= fir_x2 and sec_y <= fir_y <= sec_y2) or (fir_x <= sec_x <= fir_x2 and sec_y <= fir_y <= sec_y2):
    #     print('a')

        # first의 아랫변봐 sec의 윗변 선분 만나나 체크 / first의 윗면과 sec 아랫면만나니?
    # if (fir_x < sec_x2 < fir_x2 and fir_y == sec_y) or (fir_x < sec_x < fir_x2 and fir_y == sec_y) or \
    #         (fir_x < sec_x2 < fir_x2 and fir_y2 == sec_y) or (fir_x < sec_x < fir_x2 and fir_y2 == sec_y) or \
    #         (fir_y < sec_y < fir_y2 and fir_x2 == sec_x) or (fir_y < sec_y < fir_y and fir_x2 == sec_x) or \
    #         (fir_y < sec_y < fir_y2 and fir_x == sec_x2) or (fir_y < sec_y < fir_y and fir_x == sec_x2) :
    #     print('b')
    # 점 하나가 같으면?