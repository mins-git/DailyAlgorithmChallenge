import sys
sys.stdin = open('input.txt')


"""
A,B가 딱지치기 놀이를 함.
1. 별이 많은쪽이 이김.
2. 별의 개수가 같으면 동그라미 많은쪽이 이김
3. 별,동그라미 같고 네모 많은쪽이김
4. 별 동그라미 네모 같고 세모 다르면 세모 많은쪽 이김
5. 모두다 같으면 무승부

별 4
동그라미 3
네모 2 
세모 1

4의 개수를 찾으면되겠네?
"""

# 딱지치키 총 라운드 수
N = int(input())

#홀수번에는 a가 있을거고, 짝수번에는 b가있을거야.
arr = [list(map(int, input().split())) for _ in range(N * 2)] #[[1, 4], [4, 3, 3, 2, 1], [5, 2, 4, 3, 2, 1], [4, 4, 3, 3, 1], [4

# 앞뒤 비교하기.
for i in range(0, len(arr), 2):

    A = arr[i:i+2] # [[1, 4], [4, 3, 3, 2, 1]]
    A[0].pop(0)
    A[0].append('A')
    A[1].pop(0)
    A[1].append('B') # [[4, 'A'], [3, 3, 2, 1, 'B']]
    if A[0].count(4) > A[1].count(4) : print('A')
    elif A[0].count(4) < A[1].count(4): print('B')

    if A[0].count(4) == A[1].count(4) and A[0].count(3) > A[1].count(3) :
        print('A')
    elif A[0].count(4) == A[1].count(4) and A[0].count(3) < A[1].count(3) :
        print('B')
    elif A[0].count(4) == A[1].count(4) and A[0].count(3) == A[1].count(3) and A[0].count(2) > A[1].count(2):
        print('A')
    elif A[0].count(4) == A[1].count(4) and A[0].count(3) == A[1].count(3) and A[0].count(2) < A[1].count(2):
        print('B')
    elif A[0].count(4) == A[1].count(4) and A[0].count(3) == A[1].count(3) and A[0].count(2) == A[1].count(2) and A[0].count(1) > A[1].count(1):
        print('A')
    elif A[0].count(4) == A[1].count(4) and A[0].count(3) == A[1].count(3) and A[0].count(2) == A[1].count(2) and A[0].count(1) < A[1].count(1):
        print('B')
    elif A[0].count(4) == A[1].count(4) and A[0].count(3) == A[1].count(3) and A[0].count(2) == A[1].count(2) and A[0].count(1) == A[1].count(1):
        print('D')