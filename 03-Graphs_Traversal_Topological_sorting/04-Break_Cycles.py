def dfs(graph, node, visited):
    if node in visited:
        return
    visited.add(node)
    for child in graph[node]:
        dfs(graph, child, visited)


def path_exists(graph, source, destination):
    visited = set()
    dfs(graph, source, visited)
    return destination in visited


nodes = int(input())
graph = {}
edges = []
for _ in range(nodes):
    node, children = input().split(' -> ')
    children = children.split()
    graph[node] = children
    for child in children:
        edges.append((node, child))

removed_edges = []
edges = sorted(edges, key=lambda x: (x[0], x[1]))
for source, destination in edges:
    if destination not in graph[source] or source not in graph[destination]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)
    if path_exists(graph, source, destination):
        removed_edges.append((source, destination))
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f'Edges to remove: {len(removed_edges)}')
for source, destination in removed_edges:
    print(f'{source} - {destination}')
