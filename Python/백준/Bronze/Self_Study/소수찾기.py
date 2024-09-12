import sys
import math

sys.stdin = open('input.txt')



T = int(input())
a = list(map(int, input().split()))

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    sqrt_x = int(math.sqrt(x))
    for i in range(3, sqrt_x + 1, 2):
        if x % i == 0:
            return False
    return True

count = 0
for v in a:
    if is_prime(v):
        count += 1

print(count)
