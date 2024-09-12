import sys

sys.stdin = open('input.txt')

"""
N명의 직원이 있다.
해야할 일 N개 생김.
1 ~ N까지 해야할일 i번 직원이 j번일을하면 성공할 확률 pij

어진 일이 모두 성공할 확률”의 최댓값

"""
def dfs():



T = int(input())

for tc in range(1, T+1):

    N = int(input()) # 3
    case = [list(map(int, input().split())) for _ in range(N)] # [[13, 0, 50], [12, 70, 90], [25, 60, 100]]

    # 비율로 변환
    converted_data = [[x / 100 for x in sublist] for sublist in case] # [[0.13, 0.0, 0.5], [0.12, 0.7, 0.9], [0.25, 0.6, 1.0]]



