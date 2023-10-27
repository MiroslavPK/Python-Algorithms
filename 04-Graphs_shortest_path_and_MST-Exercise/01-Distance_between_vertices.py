from collections import deque


def bfs(graph, node, destination):
    visited = [False] * (max_node + 1)
    parents = [None] * (max_node + 1)
    queue = deque([node])
    
    while queue:
        if node == destination:
            break
        node = queue.popleft()
        for child in graph[node]:
            if visited[child]:
                continue
            visited[child] = True
            parents[child] = node
            queue.append(child)
            if child == destination:
                node = child
                break
    return parents


def find_path(parent, source, node):
    path = [destination]
    while node != source:
        node = parent[node]
        if node is None:
            break
        path.append(node)
    if len(path) == 1:
        path.clear()
    return path


n = int(input())
e = int(input())
graph = {}
pairs = []

for _ in range(n):
    source, destination = input().split(':')
    source = int(source)
    destination = [int(x) for x in destination.split(' ')] if destination else []
    graph[source] = destination

for _ in range(e):
    source, destination = [int(x) for x in input().split('-')]
    pairs.append((source, destination))


max_node = max(graph.keys())

for idx in range(e):
    source, destination = pairs[idx]
    parents = bfs(graph, source, destination)
    
    path = find_path(parents, source, destination)
    path_lgt = len(path) - 1 if destination in path else -1
    
    print('{%d, %d} -> %d' % (source, destination, path_lgt))
