import sys

sys.stdin = open('input.txt')



def is_palindrome(s):

    left, right = 0, len(s) -1 # 0부터 길이의 -1로 빼옴.
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):


    N, M = map(int,input().split())
    A = [input() for _ in range(N)]
    # 회문 찾아 출력하는 프로그램 만드시오
    # 가로세로 회문 찾으시오.
    # 델타 활용 필요.

    # M 길이의 문자열이 회문인지 확인하는 알고리즘 만들기

    # print(A) 'GOFFAKWFSM', 'OYECRSLDLQ', 'UJAJQVSYYC'

    result = ''

    # 가로순회 시작. N 만큼 순회하면됨.
    for row in A:
        for i in range(N - M + 1):
            # M 길이만큼 회문이니? 체크
            ispal = row[i: i + M]
            if is_palindrome(ispal): # 문자열을 가지고옴.
                result = ispal


    B = []

    for i in range(N):
        B.append(''.join([chars[i] for chars in A]))

    for row in B:
        for i in range(N - M + 1):
            # M 길이만큼 회문이니? 체크
            ispal = row[i: i + M]
            if is_palindrome(ispal): # 문자열을 가지고옴.
                result = ispal


        #첫번째 chars를 저장할 수 잇음.


    print(f'#{tc} {result}')





