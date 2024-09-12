import sys

sys.stdin = open('input.txt')

T = int(input())   # 테스트 케이스 갯수
result = []


for tc in range(1, T+1):
    H, W, N = map(int, input().strip().split())

    floor = N % H
    if floor == 0:
        floor = H
    room_number = (N-1) // H + 1
    
    result.append(floor * 100 + room_number)


for results in result:
    print(results)

#     #거리가 짧은방 배정 프로그램. h w n이 들어옴. n번째로 들어온 손님.
#     # 6 / 12 / 10
# # maximum으로는 w만큼 for문 작성 (뒤에 숫자 바꿔줘야함. 1.2.3.4.5호등 w만큼.)
#     #내부 for문으로 일단 h만큼 순회필요. 다 101호 배정(백의자리 이상을 바꿔줘야함.)

#     for wide in range(1, W+1):
#         for high in range(1, H+1):
#             # 만약 N이 h보다 크다면 N의값에 H를 지속적으로 빼기.
#             # 빼고 난 후 1호실 추가하기
#             if N > H :
#                 N -= H
#                 result = result + 1
#             # 만약 n이 h랑 같거나 작다면 n에 100을 곱해서  표현
#             elif N <= H :
#                 result = result + (N*100) + N
#     print(result)
