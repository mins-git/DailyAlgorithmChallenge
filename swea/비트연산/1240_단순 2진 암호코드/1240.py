import sys
sys.stdin = open('input.txt')

"""
풀이과정:
1. 배열을 받기!
    - 1.1배열의 세로만큼 반복되는 for문 작성 range(N)  #세로의 개수로 일단 배열 입력
    
2. 배열에서 암호 뽑기!
    - 2.1 중간에 56개의 0과 1의 암호 배열을 가지고 와야함.
    - 2.2 // 0 ~ 9까지의 암호는 모두 마지막 숫자가 1임. 따라서 뒤에서 부터 순회하면서 56개를 뽑아오면됨!
    - 2.3 // 뒤에서부터 뽑은 56개의 번호를 REVERSE하면 56개의 암호가 될것임.

3. 56개의 암호배열에서 숫자 뽑아내기!
    - 3-1: 번호 10개를 따로 튜플로 넣어주고 7개씩 자르면서 FOR문으로 10번 돌며 어떤 숫자가 같은지 체크.
    - 3-2: 같은 번호가 나오면 해당 번호를 PASSWORD 변수에 하나씩 저장.
    10 * 8번 돌면됨.

4. PASSWORD 8개의 번호에서 (홀수자리의 합 *3) + (짝수자리의 합) 이 10인지 체크하기
    - password[]에 0,2,4,6 = 홀수 의 합 *3
    - password[]에 1,3,5,7 = 짝수 의 합
    - 위에 두개 더한 후 10인지 체크
5. 출력하기
    - 10의 배수가 맞으면 sum(password)출력
    - 10의 배수가 아니면 0 출력하기

--------------------------------------------------------
고민의 흔적
3. 56개의 암호배열에서 숫자 뽑아내기!
    - 3-1 : IF문을 활용해서 2번째 문자가 0인지 1인지비교.
    - 3-1-1 : 0이면 가능성 [0,1,2,9] /1이면 가능성 [3, 4,5,6,7,8] 두가지로 분리
    - 3-1-2 : 0일 때의 가능성 체크 IF문 한번더 진행
            - 3번째 문자가 0이면 [5번째 문자가] [0이면] = 0 1이면 =9
            - 3번째 문자가 1이면 [4번재 문자가] [1이면] = 1 0 이면 2
    - 3-1-3 : 2번째 문자가 1일 시에 [3,4,5,6,7,8] 가능성 생김.
            - 3번째 문자가 1이면 [3,5,7,8] 0이면 [4,6]
                - 3번째 문자가 1이며 4번째 문자가 1이면  [3,5,7,8]
----------------------------------------------------------
"""

T = int(input())

for tc in range(1, T+1):
    #N: 배열의 세로 M: 배열의 가로
    N, M = map(int, input().split())

    #1. 배열을 받기!
    #- 1.1배열의 세로만큼 반복되는 for문 작성 range(N)  #세로의 개수로 일단 배열 입력
    pre_password = []
    for i in range(N):
        pre_password.append(input()) # '0000011101101100010111011011000101100010001101001001101110110000000000'

    #2. 배열에서 암호 뽑기!
    #- 2.1 중간에 56개의 0과 1의 암호 배열을 가지고 와야함.
    #- 2.2 // 0 ~ 9까지의 암호는 모두 마지막 숫자가 1임. 따라서 뒤에서 부터 순회하면서 56개를 뽑아오면됨!
    last_index = 0 # 11 : 뒤에서 부터임.
    row_num = 0 # 1
    for r in range(N): # 16번 순회하면서
        for index ,c in enumerate(pre_password[r][::-1]):
            if int(c) == 1:
                last_index = index + 1
                row_num = r
                break
        if last_index > 0:
            break

    reverse_pre_password = pre_password[row_num][::-1] # 거꾸로된 password
    pre_password = ''

    for i in range(last_index-1, last_index + 55):
        pre_password += reverse_pre_password[i]

    #- 2.3 // 뒤에서부터 뽑은 56개의 번호를 REVERSE하면 56개의 암호가 될것임.

    #3. 56개의 암호배열에서 숫자 뽑아내기!
    #- 3-1: 번호 10개를 따로 튜플로 넣어주고 7개씩 자르면서 FOR문으로 10번 돌며 어떤 숫자가 같은지 체크.
    pre_password = pre_password[::-1]

    keys = ['0001101','0011001','0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    final_password = [] #[7, 5, 7, 5, 5, 0, 2, 7]

    for i in range(0, len(pre_password), 7):
        compare = pre_password[i:i+7]
        if compare in keys:
            final_password.append(keys.index(compare))


    #- 3-2: 같은 번호가 나오면 해당 번호를 PASSWORD 변수에 하나씩 저장.
    #10 * 8번 돌면됨.

    #4. PASSWORD 8개의 번호에서 (홀수자리의 합 *3) + (짝수자리의 합) 이 10인지 체크하기
    # - password[]에 0,2,4,6 = 홀수 의 합 *3
    # - password[]에 1,3,5,7 = 짝수 의 합
    # - 위에 두개 더한 후 10인지 체크

    if (((final_password[0] + final_password[2] + final_password[4] + final_password[6]) * 3) + \
            (final_password[1] + final_password[3] + final_password[5]  + final_password[7])) % 10 == 0:
        print(f'#{tc} {sum(final_password)}')
    else:
        print(f'#{tc} 0')