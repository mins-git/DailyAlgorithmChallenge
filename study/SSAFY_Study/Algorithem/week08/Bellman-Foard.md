```python
INF = int(1e9)  # 무한대 값을 정의합니다.

def bellman_ford(vertices, edges, start):
    # 시작 정점에서 모든 정점까지의 거리를 INF로 초기화합니다.
    distances = {vertex: INF for vertex in vertices}
    # 시작 정점의 거리는 0으로 설정합니다.
    distances[start] = 0

    # 모든 엣지에 대해 |V| - 1번 릴렉스를 수행합니다.
    for _ in range(len(vertices) - 1):
        for u, v, weight in edges:
            if distances[u] != INF and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # 음수 사이클이 있는지 확인합니다.
    for u, v, weight in edges:
        if distances[u] != INF and distances[u] + weight < distances[v]:
            raise ValueError("Graph contains a negative weight cycle")

    return distances
```

```python
# 딕셔너리 컴프리헨션 없이 아래와 같이 사용 가능.
distances = {vertex: INF for vertex in vertices} # 해당 컴프리헨션을 아래와 같이 사용 가능.

# 빈 딕셔너리를 생성합니다.
distances = {}

# 각 정점에 대해 INF 값을 설정합니다.
for vertex in vertices:
    distances[vertex] = INF

```