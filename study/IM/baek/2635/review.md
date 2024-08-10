# 코드

- 문제 풀이 포인트 🤞
    1. 2번째 수를 99번 반복하며 모든 경우의수를 계산해보려고함.
    2. 최적의 해를 찾으며 max count와 for print 출력값 두개를 지속 업데이트 해줌.
- 앗 나의 실수 😢
    1. 만약 N이 100이라면 딱 99번만 찾으면 되나, for문을 하나 더 써서 계속 초과로 탐색을 했었음

```python
#1.

def su_man(N):
    global max_count
    forprint = []
    sec_num = 0


    for minus in range(1, N+1): #99까지 뺄꺼임 2번재수 100번 만들어주기

        num = [N,minus]

        # 두번째 수에서 첫번째 수를 뺀것을 세번째에 넣어주세요 를 적으면됨. 0보다 클동안만
        while True: # 0보다 클동안만 진행
            if num[-2] - num[-1] < 0: # 1번째 - 2번째값
                break
            num.append(num[-2] - num[-1])

            if max_count < len(num):
                max_count = len(num)
                forprint = num

    return (max_count, forprint)


N = int(input())
max_count = 0
result = su_man(N)

max_count, num = result

print(max_count)
print(*num)
```