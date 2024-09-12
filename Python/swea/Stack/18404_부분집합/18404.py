
import sys

sys.stdin = open('input.txt')


# 부분집합의 개수를 구하시오.
# 원소의 합이 10인 부분집합의 개수 구하시오.
def bubun(arr, s, t, i): # s: 현재합 t:목표합
    global count
    if s == t:
        count += 1
        return
    elif i >= len(arr):
        return
    elif s > t:
        return

    bubun(arr, s+arr[i], t , i + 1)
    bubun(arr, s, t, i+1)



arr = list(map(int, input().split()))
count = 0
bubun(arr,0,10, 0) # 현재 배열, 현재값 # 목표값 # 인덱스값
print(f'#1 {count}')
