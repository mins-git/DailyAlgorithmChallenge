# 교환
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def check(arr, count):
    n = len(arr)
    if count == 0:
        return int(''.join(arr))

    max_reward = 0

    for i in range(n):
        for j in range(i+1, n):
            swap(arr, i ,j)
            max_reward = max(max_reward, check(arr,count-1))
            swap(arr, i, j)

    return max_reward

# Testcase 수
T = int(input())

# Testcase 만큼 반복
for tc in range(1, T+1):

    str_len, count = map(int, input().split())
    arr = list(str(str_len))

    result = check(arr,count)
    print(f'#{tc} {result}')


