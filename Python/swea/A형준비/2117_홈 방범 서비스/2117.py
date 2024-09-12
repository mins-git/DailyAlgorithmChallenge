import sys
sys.stdin = open('input.txt')


"""
N * N 크기 도시
fig.1 

운영 비용 = K * K + (K - 1) * (K - 1)


도시크기 N과 하나의 집이 지불할 수 있는 비용 M
손해를 보지 않으면서 홈방범 서비스를 가장 많은 집들에 제공하는 서비스 영역을 찾고,

보험사의 이익 >= ((pay_bills * 제공된 집의수) - 운영비용)
위의 조건에서, 가장 많은 집들에게 제공할 수 있는 방법?


꼭 홈방범 서비스가 집위에 설치되야되진 않는거잖아? -> 완탐 진행. 

1. k = 1인 상태로 시작. k는 n까지 진행하면됨.
    1.1 k의 범위에 따라서 해당 범위에 집이 없으면, k를 증가시켜보기. n까지 
    1.2 k의 범위내에 집이 있으면 집의 개수 count진행. max를 지속 업데이트. 
    
point 1. 그럼 k의 범위는 어떻게 체크할거야?  + 그 안에 집이 있는지는 어떻게 체크할거야?

K = 4 
본인의 인덱스 home[r][c]에서 > 우측으로 range K만큼 좌측으로 range k만큼 위로 k만큼 아래로 k만큼
for i in range(N): n만큼 순회하면서 K 다 체크.
    for j in range(i, i*2-1) 까지 순회 너도 k만큼 순회하면서

home[r][c-]



2. 모든 위치에 따른 것을 업데이트 하면 max가 나올듯?
"""

def check(x, y, rhombus, home):

    rows = len(home)
    cols = len(home[0])
    cnt = 0

    for i in range(-rhombus + 1, rhombus):
        row = x + i
        # 현재 행이 배열 범위 내?
        if 0 <= row < rows:
            col_range = rhombus - abs(i)

            for j in range(-col_range +1, col_range):
                col = y + j
                if 0 <= col < cols:
                    if home[row][col] == 1:
                        cnt += 1

    return cnt

T = int(input())

for tc in range(1, T+1):
    city_size, pay_bills  = map(int, input().split())
    home = [list(map(int, input().split())) for _ in range(city_size)]
    max_house_num = 0

    for i in range(city_size):
        for j in range(city_size):
            for k in range(1, city_size+2): # k는 도시크기를 다 덮을정도까지 고려하면됨.
                # 보험사의 이익 >= ((pay_bills * 제공된 집의수) - 운영비용)
                # 운영 비용 = K * K + (K - 1) * (K - 1)
                house_cnt = check(i, j, k, home) # 제공된 집의 수임.
                profit = (pay_bills * house_cnt) - (k * k + (k - 1) * (k - 1))
                if profit >= 0:
                    max_house_num = max(max_house_num, house_cnt)

    print(f'#{tc} {max_house_num}')