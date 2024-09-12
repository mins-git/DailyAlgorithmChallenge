import sys


sys.stdin = open('input.txt')


T = input().strip()
count = 1

if T == "":
    print(0)

# for tc in range (1, T+1) :
    # " "가 보일때마다 count하면 되지 않을까?
else :
    for tc in range (len(T)):
        if " " == T[tc] :
            count += 1

    print(count)