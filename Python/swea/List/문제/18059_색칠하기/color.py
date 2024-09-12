import sys

sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):

    paint = int(input())
    red = []
    blue = []
    count = 0
    for i in range(paint):
        x1, y1, x2, y2, color = map(int, input().split())
        # 빨간색 칠하기
        if color == 1:
            for r in range(y1, y2 +1): # r 행크기만큼 순회
                for c in range(x1, x2 +1): # c 열 크기만큼 순회
                    red.append([r, c])
        # 파란색 칠하기
        elif color == 2:
            for r in range(y1, y2 + 1):  # r 행크기만큼 순회
                for c in range(x1, x2 + 1):  # c 열 크기만큼 순회
                    blue.append([r, c])

    # set으로 교집합 찾기
    red_set = set(map(tuple,red))
    blue_set = set(map(tuple,blue))

    overlapping = red_set.intersection(blue_set)
    count = len(overlapping)

    print(f'#{tc} {count}')

    # if len(red) <= len(blue):
    #   for red_color in red:
    #       for blue_color in blue:
    #           if red_color == blue_color:
    #               count +=1
    # else:
    #     for blue_color in blue:
    #         for red_color in red:
    #             if blue_color == red_color:
    #                 count += 1
    # print(f'#{tc} {count}')