import sys

sys.stdin = open('input.txt')

N = int(input())
S = list(map(int, input().split()))


min = min(S)
max = max(S)

result = [min, max]

print(*result)