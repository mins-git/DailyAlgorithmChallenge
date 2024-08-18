import sys
sys.stdin = open('input.txt')

"""
100인 정사각형 모양의 흰색 도화지가 있다.
 10x10인 색종이 붙일것임.
 
"""

# 가로세로길이 100임.
matrix = [[0] * 100 for _ in range(100)]

# 생종이 수
paper_count = int(input())
# 왼쪽 아래 x,y 들어옴.
arr = [list(map(int, input().split())) for _ in range(paper_count)]


for x,y in arr :
    for i in range (x, x + 10):
        for j in range(y, y + 10):
            if matrix[i][j] == 0:
                matrix[i][j] = 1


answer = 0
for i in range(100):
    answer += sum(matrix[i])
print(answer)