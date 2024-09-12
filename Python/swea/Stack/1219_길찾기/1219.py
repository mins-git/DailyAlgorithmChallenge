

import sys
sys.stdin = open('input.txt')

# b를 간적이 있니?

def dfs(s,v): #s는 몇번째부터 시작할거니, 최대 숫자가 뭔데?v
    stack = [] #stack이라는 배열이 필요함
    visited = [False] * (v+1) # visited로 방문한 곳 확인하기 위함.
    x = s # 현재 노드 위치 알아야겠지? 첫번재 노드부터 시작해야겟지?

    while True:
        for i in graph[x]: # 현재위치를 graph로 가지고 온 후 해당값에 인접한 노드가 있는지 찾아야돼!
            if visited[i] == False:
                stack.append(x) # 만약 방문한적없으면 stack에 채워넣고,
                x = i #현재위치를 업데이트 해줘야겠지?
                if x == 99 : #만약 x의 값이 숫자 99라면
                    print(f'#{test_case} 1')
                    return
                visited[i] = True
                break# for문 break
        else:
            if stack: #만약 스택의 값이 있으면 되돌아갈거고 해당 값을
                x = stack.pop() # 현재 위치에 넣어주면돼!
            else: #되돌아갈 곳이 없음. 즉 스택의 값이 비어있으면
                break # while문 break

    print(f'#{test_case} 0')
    return



T = 10
for tc in range(1, T+1):

    # A-B로 가는길이 존재하는지 알아내는 프로그램 작성
    # 한가지 길이라도 있으면됨. 화살표 반대 못가.

    # 출발점 0 도착점 99
    # 정점개수 98개(출발 도착 제외 합하면 총 100개)

    test_case, num_len = map(int, input().split())  # 테스트 케이스의 번호
    graph = [[] for _ in range(100)]
    arr = list(map(int,input().split()))

    # 숫자가 주어지는데, 01 02 > 이건 0이 1과 2로갈 수 있다는 말임.
    for i in range(num_len):
        v1, v2 = arr[i*2], arr[i*2+1] # v1은 앞의노드 v2는 뒤의노드
        graph[v1].append(v2)


    dfs(0, 99)




