def dfs(node, graph, visited):
    if visited[node]:
        return
    visited[node] = True

    non_tree_node = -1
    for child in graph[node]:
        if visited[child]:
            continue

        if node in forest and child not in forest:
            non_tree_node = child
        elif child in forest and node not in forest:
            non_tree_node = node

        if non_tree_node == -1:
            continue
            
        forest.add(non_tree_node)
        non_forest.remove(non_tree_node)
        dfs(non_tree_node, graph, visited)


nodes = int(input())
edges = int(input())

graph = {}

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []
    graph[source].append(destination)

start_node = int(input())

visited = [False] * (nodes + 1)
forest = set()
forest.add(start_node)

non_forest = {node for node in range(1, nodes + 1)}
non_forest.remove(start_node)

for node in graph:
    if node != start_node:
        continue
    dfs(node, graph, visited)

print(*non_forest)
