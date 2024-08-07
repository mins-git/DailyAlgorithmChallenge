import sys


sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    n = int(input()) # 색종이 수 받음
    num = n // 10 #길이 n을 10으로 나누어 채울 칸의 수 num 계산
    make_paper = [0 for i in range(num + 1)] #num+1 makepaper생성하고 요소0 초기화

    make_paper[1] = 1
    make_paper[2] = 3

    for i in range(3, num + 1):
        make_paper[i] = make_paper[i - 2] * 2 + make_paper[i - 1]

    print(f'#{tc} {make_paper[num]}')

# 어린이 알고리즘 교실 선생님 경우의 수 놀이 위해
    # 10의 배수인 N이 주어졌을때, 종이를 붙이는 모든 경우의 수를 찾으려면
    # 몇개 만들 수 있니?


    # 4가지 방법이있음.
    # 10혼자서 만들수 있니?
    # 20혼자서 만들 수 있니?
    # 10 상자를 세운 후 + 20이랑 합쳐서
    # 10 상자를 눕히 고 + 20이랑 합쳐서

    # A = [20, 10]
    # B = [20, 20]
    # count = 0
    # result = 0
    # ## A 혼자서 만들 수 있니? 세우거나 눞히거나 두개있음.
    # # 세워서 되니?
    # if N % A[1] == 0:
    #     count += 1
    # # 세우지 않고 눞혀서도 되니?
    # if N % A[0] == 0:
    #     count += 1
    #
    # ## 20 혼자서 만들 수 있니?
    # if N % B == 0:
    #     count += 1
    #
    # # 10 상자를 세운후 20이랑 합치기
    #
    #
    #
    #
