def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(child, graph, visited)


nodes_cnt = int(input())
edges_cnt = int(input())
graph = []
[graph.append([]) for _ in range(nodes_cnt)]
edges = []

for street in range(edges_cnt):
    start, end = [int(x) for x in input().split(' - ')]
    graph[start].append(end)
    graph[end].append(start)
    edges.append((min(start, end), max(start, end)))

print('Important streets:')

for start, end in edges:
    graph[start].remove(end)
    graph[end].remove(start)

    visited = [False] * nodes_cnt
    dfs(0, graph, visited)

    if not all(visited):
        print(start, end)

    graph[start].append(end)
    graph[end].append(start)

