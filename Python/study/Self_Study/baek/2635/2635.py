import sys

sys.stdin = open('input.txt')


# 첫번째 수 양의 정수 주어짐.
# 두번재 수 양의 정수 중 하나 선택
# 세번째부터는 앞의 앞의 수에서 앞의수를뺌 즉 3번째가 N이라면,
# N -2 - N-1을 뺀수가  3번째수임

# 음의 정수가 만들어지면 더이상 수를 만들지 않고 버림
# if 0 < N 만 while진행

# 첫번째 수가 주어질때 이 수에서 시작하여 규칙으로 만들어지는 최대 개수의 수들을 구하시오
# 최대 개수는 몇개일까?


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

