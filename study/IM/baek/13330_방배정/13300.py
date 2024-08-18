import sys
import math
sys.stdin = open('input.txt')


"""
남남 여여 방배정 해야함.
한방에 한명 배정 가능. but 최대 인원K 주어짐.
방에 최소개수?

해결방안:
1. 남여를 따로 모으기
2. 학년마다 K를 기준으로 나눠볼 수 있지 않을까?
2.1 k가 2일때 1학년 총 6명이면 3방이잖아? 수학적으로 계산가능!
3. 1학년부터 6학년 각각 필요한 방수 다 더하고, 
4. 여자도 다 더한 후 출력해.
"""

W = 0
M = 1

student_total_num, room_max_num = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(student_total_num)] # 앞에는 성별, 뒤에는 학년
# [1 1] [0 1]

# 한방에 room max num만큼 들어옴

men = [] # [[1, 1], [1, 1], [1, 2], [1, 3], [1, 4], [1, 3], [1, 3], [1, 5], [1, 5], [1, 6]]
women = [] # [[0, 1], [0, 2], [0, 2], [0, 3], [0, 6], [0, 5]]
men_need_room = 0
women_need_room = 0

# 1. 남여를 따로 모으기
for i in range(len(arr)):
    if arr[i][0] == M:
        men.append(arr[i])
    else:
        women.append(arr[i])


# 2. 학년마다 K를 기준으로 나눠볼 수 있지 않을까?

# count() 를 활용하면 더 쉬울듯?
# print(men.count([1,1]))

for i in range(1, 7):
    A = math.ceil(men.count([1,i]) / room_max_num)
    men_need_room += A


for i in range(1, 7):
    B = math.ceil(women.count([0,i]) / room_max_num)
    women_need_room += B

print(men_need_room + women_need_room)