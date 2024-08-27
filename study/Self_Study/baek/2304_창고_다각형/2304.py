"""
N개의 막대 기둥 존재. 폭 1m 높이 다를 수 있음.
수평부분은 반드시 한 기둥의 윗면과 닿음.
가장자리는 땅에 닿음. 오목하게 x
창고 면적이 가장 작은 창고를 만들려고한다.

기둥들의 높이가 주어진다. 가장 작은 창고 다각형의 면적을 구하시오.
"""

import sys

sys.stdin = open('input.txt')

pillar = int(input()) # 기둥 N
arr = [list(map(int, input().split())) for _ in range(pillar)]# 각 기둥의 왼쪽면의 위치를 나타내기에 +1씩하면 계산하기 쉬워짐

# x를 기준으로 sort해줘야함.
arr = sorted(arr, key=lambda x: x[0])

#가장 높은 y값을 찾기
max_index, max_arr_num = max(enumerate(arr), key=lambda x: x[1][1]) #2번째 기준으로 최대값 뽑아오기.

# 가장 높은값에 도달할때까지 리스트를 절반 잘라서
front_arr = arr[:max_index+1]
#(i+1 x값 - i의 x값) * y값 sum에 추가 top을 기준으로 y가 top보다 낮으면 top으로 *진행
top = 0
sum_area = max_arr_num[1] # 가장 높은값을 먼저 추가해주기


for i in range(len(front_arr)-1):
    if front_arr[i][1] >= top: # 만약y의 값보다 top이 더 크면?
        top = front_arr[i][1]

    if top >= front_arr[i][1]: # 만약 첫 y의값이 top보다 작거나 같으면
        sum_area += (front_arr[i+1][0] - front_arr[i][0]) * top # 답으로 곱해줘야지 그리고 더해줘.
        continue

    elif top < front_arr[i+1][1]:
        sum_area += (front_arr[i+1][0] - front_arr[i][0]-1) * front_arr[i][1] # 만약 top값보다 다음값이 더 크면 거기까지 곱해주기


#     2. 만약 가장 높은곳에 도달하면 도달한값 1 * y값 sum에 추가 #처음에 추가함.

# 리스트를 절반 자르고 reverse한 후
second_arr = arr[max_index:] #
second_arr = list(reversed(second_arr))
top = 0
# 3. 위랑 동일하게 y값을 기준으로 지붕 다 씌워주고
for i in range(len(second_arr)-1):
    if second_arr[i][1] >= top: # 만약y의 값보다 top이 더 크면?
        top = second_arr[i][1]

    if top >= second_arr[i][1]: # 만약 첫 y의값이 top보다 작거나 같으면
        sum_area += abs((second_arr[i+1][0] - second_arr[i][0])) * top # 답으로 곱해줘야지 그리고 더해줘.

    elif top < front_arr[i+1][1]:
        sum_area += abs((second_arr[i+1][0] - second_arr[i][0]-1)) * second_arr[i][1]

print(sum_area)





"""
# 생각 2 로풀기
가장 높은 y값을 찾기
리스트를 절반 잘라서
1. 가장 높은값에 도달할때까지 (i+1 x값 - i의 x값) * y값 sum에 추가 top을 기준으로 y가 top보다 낮으면 top으로 *진행.
2. 만약 가장 높은곳에 도달하면 도달한값 1 * y값 sum에 추가

리스트를 절반 자르고 reverse한 후 
3. 위랑 동일하게 y값을 기준으로 지붕 다 씌워주고 
"""



"""
# 생각1
1. arr의 길이만큼 순회하면서, 
  1.1 i의 y값이 i + 1 y 값보다 작거나 같으면 (i+1의 x값 - i의 x값-1) * i의 y값 을 sum에 저장하기   ** 첫값은 따로 더해주기
        (i+1의 y값 - i의 y값)*1로 더해주기
  1.2 i의 y값이 i +1 의 y 값보다 크면 i의 1cm * i의 y값 진행 sum에 저장하기 +
  1.2.1 i+1의 y값 (i+1의 x값 - i-1의 x값) 곱하기 * i+1의 y값으로 sum해서 저장하기 
2.
"""

