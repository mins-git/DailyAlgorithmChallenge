import sys
sys.stdin = open('input.txt')

"""
1 ~ N 까지 자연수를 이진 탐색 트리 저장.

왼쪽 서브트리의 루트 < 현재 노드 < 오른쪽 서브 중위순회

중위탐색순으로 숫자 증가.
루트값과, n//2번 노드에 저장된 값을 출력하세요. 

현재 해야되는것:
1. N 값을 노드라 생각
2. 중위탐색의 값들을 각 노드에 저장 후 출력 . 끝
"""

def inorder(node):
    if node == 0:
        return
    inorder(tree[node][0])
    global count
    count+=1
    num_arr[node] = count
    inorder(tree[node][1])


# 테스트 케이스 개수 구하기
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    num_arr = [0] * (N+1)
    tree = [[0,0] for _ in range(N+1)] # 왼쪽, 오른쪽 구분

    for i in range(1, N+1):
        if i * 2 > N:
            break
        tree[i][0] = i * 2
        if i * 2 + 1 > N:
            break
        tree[i][1] = i * 2 + 1

    count= 0
    inorder(1)
    print(f'#{tc} {num_arr[1]} {num_arr[N//2]}')

