import sys
sys.stdin = open('input.txt')

"""
문제해결:
16진수 2진수 4자리로 16진수 표현
N자리 16진수 각 자리수를 4자리 2진수로 표시하는 프로그램 작성.
2진수의 앞자리 0도 반드시 출력.


16 > 10 > 2진수로 변경하면될듯?
int() 사용후 >  bin() 사용하면됨.

-아래참고-
- int( , base(몇진수인지)) : 10진수로 변환
- bin( , base(몇진수인지)) : 2진수로 변환
- hex( , base(몇진수인지)) : 16진수로 변환
"""

T = int(input())

for tc in range(1, T+1):
    N, hexadecimal = map(str, input().strip().split())

    result = ''
    for i in range(len(hexadecimal)):
        a = int(hexadecimal[i], 16)  # 18430
        b = bin(a)
        b = b[2:]

        if len(b) < 4:
            while len(b) < 4:
                b = '0' + b
        result += b

    print(f'#{tc} {result}')

# ---------------------------- 16진수
# T = int(input())
#
# for tc in range(1, T+1):
#     N, hexadecimal = map(str, input().strip().split())
#     a = int(hexadecimal, 16) #18430
#     b = bin(a) #0b100011111111110
#     b = b.replace('b', "")
#
#     print(f'#{tc} {b}')

