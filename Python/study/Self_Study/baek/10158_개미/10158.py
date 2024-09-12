import sys
sys.stdin = open('input.txt')

"""
가로길이 w, 세로길이 H '

t시간 이후의 x,y 계산하여 출력해보기
시간이 2억까지니 하나하나 계산하는건 아닌듯


"""

w,h = map(int, input().split()) # 6 4
p,q = map(int, input().split()) # 4 1 (x,y)
time = int(input()) # 8

# 수학적으로 접근

#  x좌표 계산
x_new = (p + time) % (2*w)
if x_new > w:
    x = 2 * w - x_new
else:
    x = x_new

y_new = (q+time) % (2*h)
if y_new > h:
    y = 2*h - y_new
else:
    y = y_new

print(x,y)

# --------------------------------------------------------
#  시간초과 예상됨
# # 우측상단 /  좌측상단 / 좌측 하단 / 우측하단
# direction = [(1, 1),(-1,1), (-1,-1),(1,-1)]
# direct = 0
#
# ant_time = 0
#
#
#
# # ant 시간이 작을동안 time보다
# while ant_time < time:
#
#     nx = p + direction[direct[0]]
#     ny = q + direction[direct[1]]
#
#     ant_time += 1
#
#     # x값이 w랑 같다면, (6)
#     if nx == w:
#         direct += 1
#
#         if direct == 4:
#             direct = 0
#             continue
#         continue
#
#     # y값이 h랑 같다면 (4)
#     if ny == h:
#         direct += 1
#
#         if direct == 4:
#             direct = 0
#             continue
#         continue
#
#
#     # y값이 0이라면 (0)
#     if ny == 0:
#
#
#
#     # x값이 0이라면 (0)
#
#
# # 마지막 p,q값 출력하면됨.