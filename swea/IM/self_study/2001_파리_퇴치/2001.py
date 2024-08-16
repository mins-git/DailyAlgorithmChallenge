"""
N*N 배열에서 파리 숫자를 의미한다
M*M 파리채로 한번에 최대한 많은 파리 죽이기

M이 3이면 해당위치부터 3*3 전부 순회하면서 다 더해주면 되는거아님?  맞음




"""

import sys
sys.stdin = open('input.txt')


dr = [0,1] # 오른쪽 오른쪽 아래만 필요
dc = [1,0]

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly_matrix = [list(map(int, input().split())) for _ in range(N)]

    # (N - M +1) 의 횟수만큼 파리채 내려칠 수 있음
    dead_count = 0
    for r in range(N - M +1):
        for c in range(N - M +1): # 파리채는 여기까지만 돌아도됨.
            dead_sum = 0
            # 파리채 크기의 M * M 을 순회하기
            for x in range(M):
                for y in range(M):
                    dead_sum += fly_matrix[r+x][c+y]



            if dead_sum > dead_count:
                dead_count = dead_sum

    print(f'#{tc} {dead_count}')

