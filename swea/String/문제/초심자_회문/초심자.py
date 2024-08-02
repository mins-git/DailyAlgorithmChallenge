import sys

sys.stdin = open('input.txt')


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):



    input_srt = list(input())
    result = 1

    inlen = len(input_srt) // 2
    a = input_srt[:inlen]
    b = input_srt[inlen:]
    # inputsrt만큼 순회.

    for i in range(inlen):
        if a[i] != b[-i -1]:
            result = 0


    print(f'#{tc} {result}')





    #
    # if result == True:
    #     result = 1
    #
    # else : result = 0
    # print(f'{tc} {result}')
