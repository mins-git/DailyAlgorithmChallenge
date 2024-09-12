import sys
sys.stdin = open('input.txt')

"""
N*N 판
돌이 있거나 없을 수 있다. 5개이상 연속한 부분이 있는지 확인해보세요.

오목판정해서 오목이면 yes 오목아니면 no출력

1. 우 / 우측대각선 / 아래 / 아래쪽 대각선 4방향 순회하면서 방문했으면 +1씩 저장해줌.
2. 전체 배열 순회가 마치면 5가 되겠지? 그러면 정답이지

"""

dr = [0, 1, 1, 1] # 우측 대각선, 아래, 아래쪽 대각선 4방향 순회
dc = [1, 1, 0, -1]

def check_omok(N):
    for r in range(N):
        for c in range(N):
            for k in range(4): # 4방향항으로 다 체크하기
                count = 0

                nr , nc = r, c
                while 0<= nr < N and 0<= nc < N and arr[nr][nc] == 'o': # 오목이 이 있는곳으로 들어가야겠지?
                    count += 1 # 해당 방향으로 끝까지 가면서 체크해
                    if count ==  5:
                        return 'YES'
                    nr += dr[k] # nr의 위치를 한 방향으로 계속 진행해줘. 진행하다보면 nr이 n을 탈출하겠지?
                    nc += dc[k] # nr의 위치를 한 방향으로 계속 진행해줘. 진행하다보면 nr이 n을 탈출하겠지?

    return 'NO'

T = int(input())

for tc in range(1, T+1):

    N = int(input()) # 몇 * 몇인지 알아야하니
    arr = [input() for _ in range(N)] # arr 받아오기.

    print(f'#{tc} {check_omok(N)}')