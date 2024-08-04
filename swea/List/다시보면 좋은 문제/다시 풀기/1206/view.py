import sys
sys.stdin = open('input.txt')


# 좌우측 2거리 이상 확보되면 조망권 확보됨.
# 조망권 확보된 세대수
# if 반환 is None:


T = 10

for tc in range(1, T+1):

    building_count = int(input()) # 빌딩 수
    building = list(map(int, input().split())) # [0, 0, 254, 185, 76, 227, 84, 175, 0, 0]

    # 1번째 칸이랑, 3번째칸을 비교하면서 끝까지 가면돼.
    count = 0
    for i in range(2, building_count):
        # 좌우측 조망권이 다 확인되어야함.
        # 만약 2번째 기준으로 01번째, 34번째 체크 필요함
        if building[i] > building[i-1] and building[i] > building[i-2] and building[i]> building[i+1] and building[i]> building[i+2]:
            arr = [building[i-2],building[i-1],building[i+1],building[i+2]]

            sec_high = max(arr)

            count += building[i] - sec_high #제일 큰 builing 높이.


    print(count)