import sys
import itertools
sys.stdin = open('input.txt')

"""
7난쟁이의 키합 100

아홉 난쟁이의 키가 주어지면 백설공주 일곱난쟁이 찾아줘

7난쟁이키 아무거나 출력해
"""

height = [int(input()) for _ in range(9)] #[20, 7, 23, 19, 10, 15, 25, 8, 13]

combinations = itertools.combinations(height, 7)

valid_combination = [x for x in combinations if sum(x) == 100] #[(20, 7, 23, 19, 10, 8, 13)]

answer = sorted(valid_combination[0])

for row in answer:
    print(row)

# itertools.permutations
# 순열
# itertools.combinations()
# 조합
# itertools.combinations_with_replacement()
# 중복조합