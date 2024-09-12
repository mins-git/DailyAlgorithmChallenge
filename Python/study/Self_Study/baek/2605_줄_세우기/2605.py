import sys
sys.stdin = open('input.txt')



"""

첫번째 줄 선 학생은 무조건 0번: 제일 앞에 섬
두번째 줄 선 학생 : 0 or 1 하나를 뽑음 0이면 그자리 그대로 1이면 바로앞의 학생 앞으로
세번째줄 선 학생 : 0 ,1 ,2 0은 그대로 1은 안칸앞 2는 두칸앞
뽑은 번호는 자신이 처음 줄 선 번호보다 작은수 -1 뽑게됨.

최종 줄 선 순서 출력 
"""

student_count = int(input())
pick_num = list(map(int, input().split())) # [[0, 1, 1, 3, 2]]

line = [1]

# 학생 수 만큼 순회해야하며
for studnet in range(1, student_count):

    # 만약 0이면 바로 뒤에 추가.
    if pick_num[studnet] == 0:
        line.append(studnet + 1) # 두번재 학생 여기들어와.
    else:
        # 전체 라인에서, picknum의 student학생만큼 뺀거를 넣으면됨.
        line.insert(len(line) - pick_num[studnet], studnet + 1)


for row in line:
    print(row, end =" ")
