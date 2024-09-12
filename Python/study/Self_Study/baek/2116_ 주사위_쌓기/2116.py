import sys

sys.stdin = open('input.txt')


"""
문법:
pair['5'] 와 같이하면 value가 나옴.

옆면 숫자의 합의 최댓값을 구하시오

AF BD CE가 마주봐야함
05 13 24가 마주봐야함.

1. ARR을 돌면서 아래 주사위의 윗면이 1~6 일때에 6번 순회를 하면서
#2. 첫번째가 1이면 2번째는 아래가 1인것을 AF, BD, CD중 찾아서 두고 맞은편을 위로두고 해당과정 N-1만큼 반복
    2-1 쌓아가면서 옆면의 최댓값 을 계속 더해가기
3. 2층의 맞은편이 아래로 오고 맞은편으로두고 
"""


dice_count = int(input())
arr = [list(map(int, input().split())) for _ in range(dice_count)]
pair = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}   # 이렇게 겹침


# arr[-1] #[4, 1, 6, 5, 2, 3]
max_sum = 0

# 1. ARR을 돌면서 아래 주사위의 윗면이 1~6 일때에 6번 순회를 하면서
for i in range(6):
    top = arr[0][i]
    bottom = arr[0][pair[i]]
    sum = 0
    filter_arr = [num for idx, num in enumerate(arr[0]) if idx != i and idx != pair[i]]  # bottom과 top을 제외하고 sum해줘야지.
    sum += max(filter_arr)  # 첫번째 6개중 탑바텀을 제외하고 가장 큰값을 구하기.



# 2. 첫번째가 1이면 2번째는 아래가 1인것을 AF, BD, CD중 찾아서 두고 맞은편을 위로두고 해당과정 N-1만큼 반복
#     pair[i] # 지금은 1이겠지? pair[i] 는 값이 나올것임.
    # 주사위 횟수만큼 돌거야.
    for x in range(1, dice_count):
        bottom_idx = arr[x].index(top) # arr의 배열에서, 1층의 top의 값의 인덱스가 2층의 arr의 몇번째에 있는지 찾아서 idx를 넣어줘야함.
        bottom = arr[x][bottom_idx] # 해당 인덱스를 넣어주면 해당 바텀값이 튀어나옴.
        top = arr[x][pair[bottom_idx]] # 겹치는 pair값을 즉 마주보는값이 위로 가야겠지?


        filter_arr = [num for idx, num in enumerate(arr[x]) if idx != bottom_idx and idx != pair[bottom_idx]]
        sum += max(filter_arr)

    if sum > max_sum:
        max_sum = sum

print(max_sum)



# ----------------------------------------------------
# 필요없어진 코드
# top = str(i) # 6개 다돌거임.
# top = pair[top]
# bottom = str(i)
# filter_arr = [t for t in arr[0] if t not in (bottom, top)] # 탑바텀을 제외한 상태에서 0번째 층에서 가장 큰수 찾기
# sum = max(filter_arr) # 첫번째 6개중 탑바텀을 제외하고 가장 큰값을 구하기.


# bottom = top # 2층의 bottom은 1층의 탑이어야지.
# top = pair[bottom]
# filter_arr = [x for x in arr[x] if x != bottom and x != top] # 2층에서 가장 큰값 찾기 btm (아래),pair[btm](탑)값을 제외하고
# sum += max(filter_arr) # sum 해주면됨. 최대값을