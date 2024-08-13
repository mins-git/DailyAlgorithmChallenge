"""
    1. 화구에 3개만 넣기
    2. 나눠서 0이 생기는것이 있을때에
    3. 새로운 피자 추가해주기
    4. 화구에 피자가 1개가 남을때까지 반복해
    5. 그 1개피자 번호 출력해
"""



import sys
from collections import deque

sys.stdin = open('input.txt')


def pizza(iCi):
    hwagu = []
    queue = deque(iCi)
    pizza_num = 0

    # 1. 화구에 3개만 넣기
    for i in range(min(N, len(queue))):
        hwagu.append(queue.popleft()) # 화구에 3개의 피자 채움.

    # 2. 나눠서 0이 생기는것이 있을때에
    while len(hwagu) > 1: # 나눠서 0이생기는것이 있을때 처리.
        new_hwagu = []

        for i in hwagu:
            pizza_num, cheeze = i
            cheeze //= 2 #화구의 첫번째 요소를 // 2 해줘.

            if cheeze > 0: # 치즈양이 많으면 화구에두고
                new_hwagu.append([pizza_num,cheeze])
            else:
                if len(queue) > 0: # 새로운 피자를 추가해줄건데, queue 가 있을때만!
                    new_hwagu.append(queue.popleft()) #새로운 피자를 추가해주고 다음순회 돌아도 돼.
        hwagu = new_hwagu


    if len(hwagu) == 1:
        pizza_num = hwagu[0][0]
        return pizza_num

    return pizza_num



T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N은 화덕의 크기 M은 피자개수
    Ci = list(map(int,input().split())) # M개의 피자에 뿌려진 치즈의 양임.
    iCi = [] # [[1, 7], [2, 2], [3, 6], [4, 5], [5, 3]]  # 번호를 가지고 있어야함.
    for index, cheeze in enumerate(Ci, start=1):
        iCi.append([index,cheeze]) # 치즈 앞에 피자 번호 주어짐.

    pizza_result = pizza(iCi)

    print(f'#{tc} {pizza_result}')