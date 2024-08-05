import sys

sys.stdin = open('input.txt')


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):



    str1 = input()
    str2 = input()
    count = 0

    # XYPV 중 가장많은 chr 개수 출력
    # EOGGXYPVSY 여기에 몇개있는지 확인

    for char in str1 :
        comparison = 0
        for char_min in str2:
            if char == char_min:
                comparison += 1
        if comparison > count:
            count = comparison


    print(f"#{tc} {count}")