import sys

sys.stdin = open('input.txt')

"""
A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내림
0시부터 24시간동안 최대한 많은 화물차가 싣고 내림.

최대 몇대의 화물차가 이용 가능한지 출력

"""


def work_time(time_table):
    time_table = sorted(time_table, key=lambda x: x[1])  # [[4, 14], [8, 18], [17, 20], [20, 23], [23, 24]]

    cnt = 0
    recent_time = 0

    # 각 작업을 순회하면서 선택할 수 있는지 판단
    for start, end in time_table:
        if start >= recent_time: # 현재 작업의 시작 시간이 가장 최근 작업의 종료 시간 이후라면
            cnt +=1
            recent_time = end # 최근 선택된 작업의 종료 시간을 업데이트
    return cnt



# Testcase 수
T = int(input())
# Testcase 만큼 반복

for tc in range(1, T + 1):
    application_form = int(input())
    time_table = [list(map(int, input().split())) for _ in
                  range(application_form)]  # [[20, 23], [17, 20], [23, 24], [4, 14], [8, 18]]

    # 작업시간 s와 / 종료 시간 e

    print(f'#{tc} {work_time(time_table)}')


#------------------------------------------
# 백트래킹 , 동적 프로그래밍을 활용하여 모든 가능한 조합 도출
"""
def work_time(time_table):
    from itertools import combinations

    # 모든 가능한 작업 조합을 검사합니다.
    def is_valid(schedule):
        end_time = 0
        for start, end in schedule:
            if start >= end_time:
                end_time = end
            else:
                return False
        return True

    max_count = 0
    n = len(time_table)
    
    # 모든 가능한 조합을 생성하고 유효성을 검사합니다.
    for i in range(1, n + 1):
        for combo in combinations(time_table, i):
            if is_valid(combo):
                max_count = max(max_count, len(combo))
    
    return max_count

# 테스트 케이스 실행
time_tables = [
    [[20, 23], [17, 20], [23, 24], [4, 14], [8, 18]],  # Expected output: 3
    [[14, 23], [2, 19], [1, 22], [12, 24], [21, 23], [6, 15], [20, 24], [1, 4], [6, 15], [15, 16]],  # Expected output: 4
    [[18, 19], [2, 7], [11, 15], [13, 16], [23, 24], [2, 14], [13, 22], [20, 23], [13, 19], [7, 15], 
     [5, 21], [20, 24], [16, 22], [17, 21], [9, 24]]  # Expected output: 5
]

for time_table in time_tables:
    print(work_time(time_table))

"""