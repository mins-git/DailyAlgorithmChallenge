import sys


sys.stdin = open('input.txt')


A_Z_arr = list(input())

for char in range(len(A_Z_arr)):
    A_Z_arr[char] = ord(A_Z_arr[char]) -64

print(*A_Z_arr)