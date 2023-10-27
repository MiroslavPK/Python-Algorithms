from collections import deque


def bfs(graph, start, destination):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        if node == destination:
            break
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                queue.append(child)
                parents[child] = node
    return parents


nodes_cnt = int(input())
edges_cnt = int(input())

graph = []
[graph.append([]) for _ in range(nodes_cnt + 1)]

for edge in range(edges_cnt):
    destination, source = [int(inp) for inp in input().split()]
    graph[source].append(destination)
    graph[destination].append(source)

start_node = int(input())
destination_node = int(input())

visited = [False] * (nodes_cnt + 1)
parents = [0] * (nodes_cnt + 1)
path = deque([destination_node])

bfs(graph, start_node, destination_node)

idx = destination_node
while idx != start_node:
    path.appendleft(parents[idx])
    idx = parents[idx]

print(f'Shortest path length is: {len(path) - 1}')
print(*path)
