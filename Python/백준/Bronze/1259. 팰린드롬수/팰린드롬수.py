while True:
    S = input().strip()  # 입력을 반복적으로 받음 (strip()을 통해 앞뒤 공백 제거)
    if S == '0':  # 종료 조건, '0' 입력 시 종료
        break
    
    reversed_S = S[::-1]  # 문자열을 뒤집음

    if S == reversed_S:
        print('yes')
    else:
        print('no')
