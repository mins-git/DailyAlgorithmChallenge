import sys
sys.stdin = open('input.txt')

"""
전위순회로 해야됨.
트리 정점의 총수 V 간선 N'

"""

# 중위 순회 => 왼쪽 -> 자신 -> 오른쪽
def inorder(node):
    # 자식이 없는 경우
    if not tree[node]:
        return
    # 왼쪽에 자식이 있는지 확인
    inorder(int(tree[node][1]))
    # 문자 출력
    print(tree[node][0], end="")
    # 오른쪽에 자식이 있는지 확인
    inorder(int(tree[node][2]))



