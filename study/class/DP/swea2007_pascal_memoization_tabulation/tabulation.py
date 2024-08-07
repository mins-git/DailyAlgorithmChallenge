import sys

sys.stdin = open('input.txt')


# Testcase 수
T = int(input())
# Testcase 만큼 반복
for tc in range(1, T+1):

    N = int(input())

    # Tabulation 방식
    # Bottom-up으로 진행
    # 작은 것을 해결한 결과를 이용해서 큰 것을 해결함

    # 파스칼 위에서 부터 밑으로 내려오는 방식임.
    # 다음줄을 계산할 때에는, 원소가 하나씩 늘어남. (파스칼 삼각형이잖아?)
    # 이전 값 개수가 1개라면 계산 x
    # 이전 값 개수가 2개라면 1번 계산
    # 이전 값 개수가 3개라면 2번 계산 # 즉 계산해야되는 횟수는 이전값 개수 -1회임
    print(f'#{tc}')
    before_list = [1]
    print(*before_list)

    for _ in range(N-1): # 첫번재 줄은 이미 해결했기 때문에 N-1
        temp_list = [] # 층별로 새롭게 계산된 값이 저장되어야 하기에 초기화 위치는 N 이 반복될때 위치해야 한다.
        temp_list.append(1) # 가장 왼쪽의 1
        for i in range(len(before_list)-1): # 계산되어야 하는 횟수는 (이전 리스트의 길이 -1)
            # 두수를 합해서 temp_list에 저장
            result = before_list[i] + before_list[i+1] # 그냥 가독성을 높이기위해서 변수를 넣은것임
            temp_list.append(result)
        temp_list.append(1)

        # print(temp_list)
        before_list = temp_list # 다음 값을 계산하기 위해 현재 계산된 값을 before에 저장
        print(*before_list)