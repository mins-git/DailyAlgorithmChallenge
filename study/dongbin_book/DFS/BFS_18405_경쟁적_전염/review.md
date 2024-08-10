# 코드

- 문제 풀이 포인트 🤞
    1. BFS를 활용하여 S로 받은 시간초에 따른 너비우선탐색을 진행하면 됨.
    2.
- 앗 나의 실수 😢
    1. PyCham에서는 정상 작동되었으나, 백준기준으로 시간초과발생.
    -  따라서 while문을 없애고 for문으로 S시간초만큼만 순회하기로 코드 변경
    - sorted() 등과 같은 파이썬 기본함수는 최대한 사용하지 않으려 버블정렬을 이용하였었으나, 시간 초과로 인한 문제이기에, 버블정렬 대신 sorted()를 사용하였다.


```python

N, K = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
S, X, Y = map(int,input().split()) #각자 잘들어와야됨

# start_point = [(r, c) for r in range(N) for c in range(N) if matrix[r][c] != 0]



def bfs(matrix,N,S):
    # 이 스타트 포인트는 전체 값을 가지고 오잖아?
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

    queue = deque()
    for r in range(N):
        for c in range(N):
            if matrix[r][c] != 0:
                queue.append((matrix[r][c], r, c)) # 바이러스 값도 입력
    queue = deque(sorted(queue)) # 번호에 따른정렬 sorted써야 시간복잡도 줄임.
    for _ in range(S):
        length = len(queue)
        for _ in range(length):
            virus_num, recent_x, recent_y = queue.popleft()  # x,y 좌표를 넣어주면 됨. 각 값이 들어있을거잖아 아직 퍼지기 전.
            for dr, dc in directions:
                new_x, new_y = recent_x + dr, recent_y + dc
                if 0 <= new_x < N and 0 <= new_y < N and matrix[new_x][new_y] == 0:
                    matrix[new_x][new_y] = matrix[recent_x][recent_y]  # 현재값을 새로운곳에 넣어줘바 상하좌우로
                    queue.append((virus_num, new_x, new_y))
    return matrix
   
matrix = bfs(matrix, N,S)
print(matrix[X-1][Y-1])
```