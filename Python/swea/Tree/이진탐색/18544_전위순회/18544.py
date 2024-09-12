import sys
sys.stdin = open('input.txt')

"""
첫줄에는 트리의 점점의 총수 vertex가 주어짐.
다음줄은 간선 나열. (부모-자식)순서
"""


Vertex = int(input())
arr = list(map(int, input().split()))

left = [0] * (Vertex+1)
right = [0] * (Vertex+1)

for i in range(0, len(arr), 2):
    parent, child = arr[i], arr[i+1]
    if left[parent] == 0:
        left[parent] = child
    else:
        right[parent]= child

def preorder(node):
    if node == 0:
        return
    else:
        print(node, end = ' ')
        preorder(left[node])
        preorder(right[node])


preorder(1)