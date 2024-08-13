"""
8개의 숫자 입력
1감소후 제일뒤로
2를 감소하고 제일뒤로
...
5를 감소하고 제일뒤로로

0보다 작아지는 경우 0으로 유지. 프로그램 종료됨.
이때의 8자리 숫자의 값이 암호

"""


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