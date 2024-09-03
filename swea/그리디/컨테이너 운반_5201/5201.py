import sys
sys.stdin = open('input.txt')

"""
N개의 컨테이너를 m개의 트럭으로 A > B 이동
트럭당 한개의 컨테이너 운반 가능. 트럭의 적재 용량을 초과하는 컨테이너 운반 X
컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량
m대의 트럭이 한번만 운행

화물의 총 중량이 최대! 

컨테이너를 한개도 옮길 수 없는 경우 0 을 출력하면 됨.

sort 두개하고 큰수대로 끼워넣으면 문제생길듯?
"""


def load(object_weight, loading_capacity):
    load_weight = 0
    object_weight = sorted(object_weight, reverse= True) # [5, 3, 1]
    loading_capacity = sorted(loading_capacity, reverse= True) # [8, 3]

    i, j = 0, 0

    while i < len(loading_capacity) and j < len(object_weight):
        if loading_capacity[i] >= object_weight[j]:
            load_weight += object_weight[j]
            i += 1  # 다음 수로 이동
        j += 1  # j는 그냥 항상 이동하면됨
    return load_weight


T  = int(input())

for tc in range(1, T+1):

    # 컨테이너 수 / 트럭 수
    container_count, truck_count = map(int, input().split()) # 3 2
    # container개의 화물의 무게 들 /
    object_weight = list(map(int, input().split())) # 1 5 3
    # truck개의 트럭 적재 용량 tj
    loading_capacity = list(map(int, input().split())) # 8 3

    print(f'#{tc} {load(object_weight, loading_capacity)}')















