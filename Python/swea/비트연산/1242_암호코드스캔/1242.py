import sys
import re
sys.stdin = open('input.txt')

"""
세로 2000, 가로 500 직사각형 암호코드 전달.

세로 길이는 5~100칸
비율로 계산하시오.

홀수 자리의 합 * 3 + 짝수자리의 합 + 검증코드 = 10의배수
검증코드는 6이된다면 정상적인 암호 코드다.

1 세로 2000, 가로 500  이하의 직사각형 배열에 암호코드 정보가 포함되어 전달됨.

2. 배열 : 16진수 > 2진수로 변환하여 > 안의 암호코드 확인
3. 비정상적인 코드가 있지만, 1개이상의 암호코드는 있긴함
4. 고유번호와 검증번호르 확인해 정상여부를 판단하고 정상 암호코드의 합 출력
5. 총 소요시간 적을수록 좋음.

1개의 암호코드는 숫자 8개 7개 고유번호 + 1개 검증코드

암호코드는 56의 배수로 들어옴 
56이면 7개로 진행 112개면 14개로 체크필요

56나누기 암호코드 가로길이의 몫만큼 암호의 개수가 있음.



문제해결 과정.
1. 배열 받기 # 0 이아닌것만 솎아내기
2. 배열은 16진수로 이루어져 있으며, 이 배열을 2진수로 변환
2.1 
"""

# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]


    password_row = []
    # 0이 아닌것만 찾아내기기
    for i in range(N):
        if any(char != '0' for char in arr[i]): # ['000000001DB176C588D26EC000', '000000001DB176C588D26EC000',]
            password_row.append(arr[i])

    password_row = list(set(password_row)) #['000000000000000000000000000196EBC5A316C57800000000', '000000328D1AF6E4C9BB0000000196EBC5A316C57800000000']

    password_bin = ""
    for i in range(len(password_row)):
        password_bin += password_row[i]


    password_bin = bin(int(password_bin, 16))
    password_bin = password_bin[2:].rstrip('0')
    print(password_bin)

    # 찐 비밀번호
    real_password = set()

    while len(password_bin) >= 0:
        for i in range(len(password_bin), 0, -1):
            if i == 1:

        real_password.add(password_bin[i-56:i])
        password_bin = password_bin[:i-55]


    print(real_password)