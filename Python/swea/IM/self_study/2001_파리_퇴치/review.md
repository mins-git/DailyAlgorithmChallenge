# 코드

- 문제 풀이 포인트 🤞
    1. 파리채의 크기를 M*M 순회해야 할 때에, r에서 + x칸만큼 더 이동해야하며, c에서 + y칸 더 이동해야함을 정확히 이해하는 과정이 필요했다.
- 앗 나의 실수 😢
    1. 
    2. 

```python
#1.
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

```