import sys

sys.stdin = open('input.txt')

A, B, V = map(int, input().strip().split())

A, B, V

# V / (A-B) = 하루동안 오를 수 있는 양. 몫 
date = 0
long = 0


if V / (A-B) <= long :
    print(date)
else: long + 





# 정답이나, 시간초과
# A, B, V = map(int, input().strip().split())

# date = 0
# long = 0

# while long < V :

#     date += 1
#     long = long + A

#     if(long >= V):
#         break
#     long = long - B
# print(date)

