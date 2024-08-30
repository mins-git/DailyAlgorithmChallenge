import sys
sys.stdin = open('input.txt')

"""
문제풀이:
0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고한다
print((1*2**-1))

2씩 곱해가면서 뽑아오기.
만약 처음 값이랑 같으면 정지 
0.625
"""


T = int(input())

for tc in range(1, T+1):

    N = float(input())
    compare = N
    i = 0
    check = False
    result = ''
    while True:
        i += 1

        if i >= 13:
            check = True
            break

        if N * 2 >= 1: # 0보다크면 1 더하기
            result += '1' # 1.25
            N = (N * 2) - 1
            # if N == 0:
            #     break
        elif 0 < N * 2 < 1 : # 1과 0 사이면
            # if N == compare: # 만약 값이 같아지면 탈출해야됨. 무한으로 가기 때문.
            #     break
            result += '0'
            N = N * 2 # N 또진행.
        if N == 0:
            break

    if check:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {result}')
