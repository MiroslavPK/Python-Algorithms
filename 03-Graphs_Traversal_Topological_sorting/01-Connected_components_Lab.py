def dfs(graph, node, visited, component):
    if visited[node]:
        return
    visited[node] = True
    for child in graph[node]:
        dfs(graph, child, visited, component)
    component.append(node)


graph = []
nodes = int(input())

for _ in range(nodes):
    graph.append([int(n) for n in input().split()])


visited = [False] * nodes

for node in range(nodes):
    if visited[node]:
        continue
    component = []
    dfs(graph, node, visited, component)
    print(f'Connected component: {" ".join([str(n) for n in component])}')
