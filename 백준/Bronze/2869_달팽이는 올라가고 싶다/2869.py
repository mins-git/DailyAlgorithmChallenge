import sys

sys.stdin = open('input.txt')


# Testcase 수

A, B, V = map(int, input().split())

# 달팽이가 정상에 도달하는 데 걸리는 일수를 계산
# V - B : 마지막 날 밤에 내려가지 않으므로 V에서 B를 뺀다.
# A - B : 달팽이가 하루 동안 실질적으로 올라가는 거리 (낮 동안 올라가고 밤 동안 내려가는 차이)
# (V - B) / (A - B) : 실질적으로 올라가야 할 거리(V - B)를 하루에 올라가는 거리(A - B)로 나누어 걸리는 날 수를 계산
if (V - B) % (A - B) == 0:
    days = (V - B) // (A - B)  # 정확히 나누어 떨어지면 몫을 그대로 사용
else:
    days = (V - B) // (A - B) + 1  # 나머지가 있으면 하루를 더 추가

print(days)

# 엄청 큰수도 올 수 있음체크
# while height < V :
#     count += 1
#     height += A
#     if height >= V:
#         break
#     height -= B
#
# print(count)

