import sys

sys.stdin = open('input.txt')


# Testcase 수


    # 가로,세로방향 1cm마다 점선이 그어져있다.

# 위 > 아래 1번부터 번호가 붙여있고 왼 > 오

# 가로 세로길이, 잘라야할 점선들. 가장큰 종이 조각 몇cm2?


row, col = map(int,input().split())
cut_count = int(input())
cut_list = [list(map(int, input().split())) for _ in range(cut_count)] #[[0, 3], [1, 4], [0, 2]]


# for i in range(cut_count):
#가로로 자르는 점선은 0과 전선 번호
#세로는 1과 점선번호