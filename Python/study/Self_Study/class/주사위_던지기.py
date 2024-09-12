"""
주사우 눈금 n개를 던져서 나오는 모든 조합을 출력
주사위 눈금 3개 => 주사위가 3개
조합
6C3 => 6개의 임의의 수에 3개가 나올 확률임.
"""

N = 3
path = []

def jusawii(lev, start):
    if lev == N:
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        jusawii(lev + 1,i)
        path.pop()

jusawii(0,1)