# 코드

- 문제 풀이 포인트 🤞
    1. count가 입력된 k와 같을때에, matrix는 배열의 끝으로 끝나거나, 검은색이어야 하며, r,c 의 앞부분도 배열의 끝에 부딪혀있거나,  검은색이라면 끝이라고 표현할 수 있다. 그 사이의 값에서 +1 해줘야함.
    2. 
- 앗 나의 실수 😢
    1. 
    2. 

```python
#1.
import sys
sys.stdin = open('input.txt')

# N * N 단어의 퍼즐을 맞춰보려고한다.

dr = [0, 1] # 오아
dc = [1, 0]

B = 0
W = 1

# 테스트 케이스 주어짐
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split()) # n= 5, k= 3
    matrix = [list(map(int, input().split())) for _ in range(N)] # N
    result_count = 0
    # 흰색은 1 검은색 0
    # 흰색에 적을 수 있는 k 찾는것임!

    # 배열을 순회하면서
    for r in range(N):
        for c in range(N):
            for k in range(2):
                nr, nc = r, c
                count = 0
                while 0<= nr < N and 0<= nc < N and matrix[nr][nc] == W : #배열을 벗어나지 않고, 검은색이 아니면,

                    count += 1 # 카운트 더해주기.
                    nr = nr + dr[k]
                    nc = nc + dc[k]

                if count == K:
                    # 검은색 또는 배열의 끝으로 끝나거나
                    if (nr >= N or nc >= N or matrix[nr][nc] == B) and \
                            (r - dr[k] < 0 or c - dc[k] < 0 or matrix[r - dr[k]][c - dc[k]] == B):  # 앞에부분이 배열을 벗어나거나, 검은색이라면
                        result_count += 1

    print(f"#{tc} {result_count}")
```