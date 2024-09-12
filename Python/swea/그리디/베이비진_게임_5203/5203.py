import sys
sys.stdin = open('input.txt')

"""
0 부터 9까지 숫자 카드 4세트 섞기 > 6개의 카드 고름
연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet.

먼저 run or triplet이면 승자
무승부 = 0 출력
승자 누구? 출력
"""



def continus_num(player):
    sort_player = sorted(player)
    for i in range(len(sort_player)-2):
        if (sort_player[i]+1 in sort_player) and (sort_player[i]+2 in sort_player) and (sort_player[i] in sort_player):
            return True
    else:
        return False

# 같은 숫자 몇개인지 체크
def same_num(player):
    for i in range(len(player)):
        if player.count(i) >= 3:
            return True
    else:
        return False

def win_check(player):

    if same_num(player): #TRUE이면,
        return True
    elif continus_num(player):
        return True
    else:
        return False

def playgame(player1, player2):
    rounds = len(versus) // 2 # 몇판 진행할건지

    for i in range(3, rounds + 1):
        player1_check = win_check(player1[:i])
        player2_check = win_check(player2[:i])

        # if player1_check and player2_check: # True 이면
        #     return 0
        if player1_check:
            return 1
        elif player2_check:
            return 2

    return 0


T = int(input())
for tc in range(1, T+1):

    versus = list(map(int, input().split()))  # [9, 9, 5, 6, 5, 6, 1, 1, 4, 2, 2, 1]

    player1 = [] # [9, 5, 5, 1, 4, 2]
    player2 = [] # [9, 6, 6, 1, 2, 1]

    for i in range(len(versus)):
        if i % 2 == 0:
            player1.append(versus[i])
        else:
            player2.append(versus[i])


    print(f'#{tc} {playgame(player1, player2)}')