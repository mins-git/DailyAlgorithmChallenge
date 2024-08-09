# 코드

- 문제 풀이 포인트 🤞
    1. 가지치기를 잘해야함(백트래킹)을 잘해야 필요없는 연산을 안 하게된다.
    2. 
- 앗 나의 실수 😢
    1. 굳이 목표합을 계속 가지고있을필요도없고, 솔직히 검사하고싶은 배열과, 인덱스만 가지고도 풀이가 가능할것 같다.
    2. 

```python
#1.

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

```