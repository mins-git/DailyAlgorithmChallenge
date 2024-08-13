# 코드

- 문제 풀이 포인트 🤞
    1. deque 덱 사용으로 for문으로 1부터 5까지 차례로 순회하며 큐 자료구조에 따라 처음 요소을 pop하고, 마지막에 append 해주기! 
    2. 
- 앗 나의 실수 😢
    1. 덱 사용시 꼭 list로 변환해서 출력해주기!
    2. 

```python
#1.

import sys
from collections import deque

sys.stdin = open('input.txt')

T = 1

def que_que(password):

    queue = deque(password)  # password 진행

    while queue[-1] >= 0:  # 큐의 마지막이 0보다 클동안

        if queue[-1] <= 0:  # 만약 queue 7번째가 0보다 작거나 같으면 끝내.
            break

        for i in range(1, 6):  # 1부터 6까지 회전

            first = queue.popleft() - i  # 왼쪽에서 i만큼빼
            if first <= 0:  # 만약 first도 0보다 작아지면
                first = 0
                queue.append(first)
                break

            queue.append(first)

            if queue[-1] <= 0:  # 만약 queue 7번째가 0이면 끝내고
                break

    return list(queue)

for tc in range(1, T+1):
    testcase = int(input())
    password = list(map(int, input().split())) # 비밀번호 리스트

    result = que_que(password)
    result = ' '.join(map(str, result))

    print(f"#{testcase} {result}")

```