# 코드

- 문제 풀이 포인트 🤞
    1. 한 방향으로 계속 진행하면서 개수를 체크해야함을 잘 파악하기
    2. 8방향 돌 필요없이 4회전만 해도 가능합니다! 한방으로 쭉 진행하기때문에 가능해요!
- 앗 나의 실수 😢
    1. 델타로 한 위치에서 4회전을 하는것이 아니라, 한위치에서 한방향으로 체크를해야 오목인지 확인이 가능함을 인지하고 풀어야했다!
    2. 

```python
#1.
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
```