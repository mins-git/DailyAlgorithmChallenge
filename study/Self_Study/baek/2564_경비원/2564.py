import sys
sys.stdin =open('input.txt')




"""

블록의 크기와 상점의 개수, 동근이의 위치 주어지면, 각 상점 사이의 최단거리의 합?

동근이의 위치와 각 상점사이의 최단거리의 합?
북쪽 남쪽인 경우 왼쪾 경계로부터의 거리 / x좌표를 의미
동쪽 혹은 서쪽인 경우 위쪽경계부터의 거리  / y좌표를 의미 

첫째 줄에 동근이의 위치와 각 상점 사이의 최단 거리의 합을 출력

결국 동근이로부터 가장 가까운 거리들의 합을 출력하면됨.

"""


# 가로 세로 길이 input됨
c, r = map(int,input().split())

store_num = int(input())
shop = [list(map(int, input().split())) for _ in range(store_num)] # [[1, 4], [3, 2], [2, 8]]
dong_goen = list(map(int,input().split())) # 현재 동근이는 남쪽 3에 위치. #[2, 3]

sort_shop = sorted(shop, key = lambda x : x[0])

# 일차원 배열로 나열해서 어디가 가까운지 체크 가능함.
def get_line(direction, distance):

    if direction == 1:
        return distance

    elif direction == 4:
        result = c + distance
        return result
    elif direction == 2:
        result = c + r + (c - distance)
        return result
    elif direction == 3:
        result = c + r +  c + (r - distance)
        return result


# 동근이의 위치 찾기.
dong_goen = get_line(dong_goen[0],dong_goen[1])  # 22
shop_list = [] # [4, 28, 17]

for i in range(len(shop)):
    shop_list.append(get_line(shop[i][0], shop[i][1]))

doulle_sum = ((c * 2) + (r * 2)) # 둘레길이

# 일단 왼쪽만 비교해보자.
answer = 0

for i in shop_list:

    sigae = abs(i - dong_goen) # 동근이 거리부터 시계방향
    bansigae = doulle_sum - sigae

    min_sum = min(sigae, bansigae)
    answer += min_sum


print(answer)












# 생각을 바꿔보자
# ------------------------------------------------------
"""
dong이 2에있을때.

1. dong 2 > 1의값
if r //2 > 1의값
    dong + r + 1의값
elif r//2 < 1의값
    c-dong + r + r-1의값

2. dong == 2의값

    abs(dong - 2의값)
    
3. dong > 3의값
    dong + r-3의값
    
4. dong > 4의값
    c-dong + r-4의값
"""
#
# for i in range(len(shop)):
#     for j in range(2):
#         if shop[i][j] == 1 : # 첫번째 값이 1이라면
