import sys
sys.stdin = open('input.txt')

"""
같은 조 참여하고 싶은 사람 출석번호 제출

한 사람이 여러 장의 종이 제출 or 여러 사람이 한 사람을 지목한 경우 모두 같은 조

적지도 않고 지목되지도 않으면 단독 조.

N 번까지의 출석번호 + m장의 신청서 제출 받음. 몇개의 조 생성됨?
"""

#1.
def make_set(n):
    p = [i for i in range(n + 1)] # 각 원소의 부모를 자신으로 초기화
    r = [0] * (n + 1)# 시작 rank는 모두 0으로 초기화
    return p, r

def find(x):

    # 원소의 부모가 자기 자신이다 == 자기가 그 그룹의 대표자임.
    if parents[x] == x:
        return x

    # 경로를 압축해줌. (path compresstion)을 통해서 부모를 루트로 설정함.
    # parents[x] # x 가 가리키고 있는 부모
    # find(parents[x]) # x의 부모로부터 대표자를 찾기.
    parents[x] = find(parents[x])
    return parents[x]  # 부모를 계속해서 재귀를 통해 찾아가는 중임.


def union(x,y):
    root_x = find(x)  # x의 부모를 찾아서 root_x에 넣기
    root_y = find(y) # y의 부모를 찾아서 root_y에 넣기

    if root_x == root_y: # 이미 같은 집합이면 끝
        return

    # rank를 비교해서 더 작은 트리를 큰 트리 밑에 병합해주기.
    # 같은 부모를 바라보게 하는거지.
    if ranks[root_x] > ranks[root_y]:
        parents[root_y] = root_x

    elif ranks[root_x] < root_y:
        parents[root_x] = root_y

    else:
        # rank 가 같으면 한쪽을 다른 한쪽에 병합하고 rank를 증가시킴
        parents[root_y] = root_x
        ranks[root_x] += 1 #x의 랭크를 높여주는 대신에 root_x 부모시켜주기.


T = int(input())

for tc in range(1, T+1):
    attendance_number, application_form = map(int, input().split()) # N번까지의 출석번호, M장의 신청서
    # application_form을 기준으로 쌍임.
    form_list = list(map(int, input().split()))

    # 각 원소의 부모를 자기 자신으로 초기화 시켜주고, rank 초기화 시켜주기
    parents, ranks = make_set(attendance_number)
    # [0, 1, 2, 3, 4] parents
    # [0, 0, 0, 0, 0] ranks

    for i in range(application_form):
        x, y = form_list[i * 2], form_list[i * 2 + 1]
        union(x, y)

    unique_roots = set()
    for x in range(1, attendance_number+1):
        root = find(x)
        unique_roots.add(root)

    print(f'#{tc} {len(unique_roots)}')


# ---------------------------------------------------------
# #2.
# def make_set(n):
#     p = [i for i in range(n)] # 각 원소의 부모를 자신으로 초기화
#     r = [0] * n # 시작 rank는 모두 0으로 초기화
#     return p, r
#
# def find(x):
#
#     # 원소의 부모가 자기 자신이다 == 자기가 그 그룹의 대표자임.
#     if parents[x] == x:
#         return x
#
#     # 경로를 압축해줌. (path compresstion)을 통해서 부모를 루트로 설정함.
#     # parents[x] # x 가 가리키고 있는 부모
#     # find(parents[x]) # x의 부모로부터 대표자를 찾기.
#     parents[x] = find(parents[x])
#     return parents[x]  # 부모를 계속해서 재귀를 통해 찾아가는 중임.
#
#
# def union(x,y):
#     root_x = find(x)  # x의 부모를 찾아서 root_x에 넣기
#     root_y = find(y) # y의 부모를 찾아서 root_y에 넣기
#
#     if root_x == root_y: # 이미 같은 집합이면 끝
#         return
#
#     # rank를 비교해서 더 작은 트리를 큰 트리 밑에 병합해주기.
#     # 같은 부모를 바라보게 하는거지.
#     if ranks[root_x] > ranks[root_y]:
#         parents[root_y] = root_x
#
#     elif ranks[root_x] < root_y:
#         parents[root_x] = root_y
#
#     else:
#         # rank 가 같으면 한쪽을 다른 한쪽에 병합하고 rank를 증가시킴
#         parents[root_y] = root_x
#         ranks[root_x] += 1 #x의 랭크를 높여주는 대신에 root_x 부모시켜주기.
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     attendance_number, application_form = map(int, input().split()) # N번까지의 출석번호, M장의 신청서
#     # application_form을 기준으로 쌍임.
#     form_list = list(map(int, input().split()))
#
#     # 각 원소의 부모를 자기 자신으로 초기화 시켜주고, rank 초기화 시켜주기
#     parents, ranks = make_set(attendance_number)
#     # [0, 1, 2, 3, 4] parents
#     # [0, 0, 0, 0, 0] ranks
#
#     for i in range(0, len(form_list), 2):
#         # 현재 인덱스에서 n 길이만큼 슬라이스하여 서브리스트를 만들고 결과 리스트에 추가
#         x, y = form_list[i] - 1, form_list[i + 1] - 1
#         union(x,y)
#
#     unique_roots = set()
#     for x in range(attendance_number):
#         root = find(x)
#         unique_roots.add(root)
#
#     print(f'#{tc} {len(unique_roots)}')
#

# ----------------------------------------------------------------------------

"""
0 - BASED로하면 X, Y 에 1을 빼줘야하지만,
MAKE_SET에 +1을 해주고 마지막에 인덱스를 기준으로 전부 가지고 오면서
결과적으로 인덱스를 기준으로 체크해볼 수 있다.

    # for i in range(0, len(form_list), 2):
    #     # 현재 인덱스에서 n 길이만큼 슬라이스하여 서브리스트를 만들고 결과 리스트에 추가
    #     x, y = form_list[i] - 1, form_list[i + 1] - 1
    #     union(x,y)
"""