import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1,T+1):
    # 문자열 입력 개수 N
    N = int(input())
    bit = '' # 0000000111100000011000000111100110000110000111100111100111111001100111

    for i in range(N):
        bit += (input().strip())

    bit = bit.strip()

    result= []
    for i in range(0, len(bit), 7):
        compare = bit[i:i+7]
        result.append(int(compare, 2))

    print(f'#{tc}', end = " ")
    for i in range(len(result)):
        print(f'{result[i]}', end=" ")
