import sys
sys.stdin = open('input.txt')


def girl(switch_num):
    i = 1

    while True:
        if switch_num - i < 0 or switch_num + i >= len(switch): #만약  switch num값이 0보다 작아지거나, switch보다 커지면 종료
            break

        if switch[switch_num-i] == switch[switch_num+i]: #만약 스위치 넘버의 양쪽이 같으면
            # 바꿔줘.
            switch[switch_num - i] = 1 - switch[switch_num - i]
            switch[switch_num + i] = 1 - switch[switch_num + i]
            i += 1
        # 그냥 리턴하면됨.
        else :
             break

    switch[switch_num] = 1 - switch[switch_num]


switch_count = int(input())
switch = list(map(int, input().split()))
student_count = int(input())
turn_on_off = [list(map(int,input().split())) for _ in range(student_count)] # 끄고 키고 배열


for i in turn_on_off: # 끄고 킨 배열 그냥 불러오기
    gender, switch_num = i # switch num에는 인덱스가 들어옴
    switch_num -= 1 # 1이랑 3이들어왓지만 2번은 이덱스값으로 드 ㄹ어옴

    if gender == 1: # 남자일 때에 스위치
        for x in range(1, (len(switch)//(switch_num+1))+1): # 스위치의 넘버만큼만 돌아도돼. 백트레킹 해야지? # 2번돌것임.
            idx = switch_num + (switch_num +1) * (x - 1)
            # switch num는 값이지만 인덱스를 탐색하잖아?  그러니 배수를 체크하기위해 위에서 빼준 1을 다시 더해주고 x에서 1을빼주면돼
            if idx < len(switch):  # 인덱스 범위 체크
                switch[idx] = 1 - switch[idx]


    elif gender == 2 :# 여자일때에 스위치
        girl(switch_num)


size = 20
for i in range(0, len(switch), size):
    print(' '.join(map(str, switch[i:i + size])))








