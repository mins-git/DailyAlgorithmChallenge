import sys

sys.stdin = open('input.txt')

# A = int(input())
# B = int(input())
# C = int(input())

# multiply = (A * B * C)

# #10개 출력해야지.
# count_digits = [0] * 10

# for digit in str(multiply):
#     count_digits[int(digit)] +=1

# for digit in range(10):
#     print (count_digits[digit])

A = int(input()) * int(input()) * int(input())

for i in range(10):
    print(str(A).count(str(i)))
