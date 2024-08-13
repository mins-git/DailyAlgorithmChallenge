# 코드

- 문제 풀이 포인트 🤞
    1. 주사위는 어차피 총 6번 돌게 될것이다. arr의 첫번째 요소인 0의 임이의 i값을 가지고오고, pair로 값을 찾아와 bottom을 업데이트 해주었다.
    2. 가장 중요한 포인트는 내 코드는 인덱스를 참조하여 최대값을 구하고 다음 top이 뭘지 찾는 코드이다. 
- 앗 나의 실수 😢
    1. bottom과 top의 값을 가져올때에, 처음에는 인덱스로 가지고오지 않고, 값을 그냥 집어넣어 갱신 방식에 문제가 있어 계속 오답이 나왔다.
       top 과 bottom의 인덱스 참조를 통해 주사위의 값을 가지고 오도록 했다. 
    2. 

```python
#1.

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
```