import sys

sys.stdin = open('input.txt')


T = int(input())


for i in range(T):
    data = input().split()

    R = int(data[0])
    S = str(data[1])

    result = ""
    for word in S :
        result = result + word * int(R)
    print(result)
