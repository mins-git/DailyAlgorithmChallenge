# 코드

- 문제 풀이 포인트 🤞
    1. 이동 방향에 따른 행을 업데이트를 할 때에, 어떤 부분에서 dr과 dc를 업데이트 해줄지 정확한 위치 파악이 필요했던 문제였다. 
    2. 
- 앗 나의 실수 😢
    1. 
    2. 

```python
#1.

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split()) # N 줄에 걸쳐 M개씩 풍선이등 종이 꽃가루 주어짐
    arr = [list(map(int,  input().split())) for _ in range(N)] #꽃가루 개수
    max_flower_count = 0

    for r in range(N): # row만큼 순회
        for c in range(M): # col 만큼 순회
            flower_sum = arr[r][c]
            for dr, dc in [[0,1], [1,0], [0, -1], [-1, 0]] :
                nr, nc = r, c
                for p in range(arr[r][c]): # 방향만큼 다 더하면되잖아?
                    nr += dr
                    nc += dc
                    if 0 <= nr < N and 0 <= nc < M: # 범위를 벗어나지 않으면,
                        flower_sum += arr[nr][nc]
                    else: break

            if flower_sum > max_flower_count:
                max_flower_count = flower_sum

    print(f'#{tc} {max_flower_count}')
```