import sys

sys.stdin = open('input.txt')

T = int(input())   # 테스트 케이스 갯수



# input만큼 순회하는 for문
for tc in range(1, T+1):
    space =""
    star = ""
    # t-1만큼 " " 추가하기.
    # space에 4개의 빈칸이 생길것임. 
    for tc2 in range(T - tc):
        space += " "

    for tc3 in range(tc):
        star += "*" 

    print(space+star)

