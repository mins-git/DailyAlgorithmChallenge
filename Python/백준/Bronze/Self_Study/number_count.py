import sys

sys.stdin = open('inut.txt')

A, B, C = map(int,input().strip().split("\n"))

multipl = A * B * C
str_multipl = str(multipl)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1~9까지의 숫자가 얼마나 쓰였니? 체크해야되는 코드.
for tc in range (len(str_multipl)):
    for num in range(tc):
        if num == numbers[num]:
            numbers[num] += 1
            #여기에서 숫자로 변수를 저장해버리면, 나중에 불러올 수가 없음. 

