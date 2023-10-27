class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


def find_path(parent, cur_node, source):
    path = [cur_node]
    while True:
        cur_node = parent[cur_node]
        path.append(cur_node)
        if cur_node == source:
            break
    return list(reversed(path))


nodes_cnt = int(input())
edges_cnt = int(input())
graph = []
[graph.append([]) for _ in range(nodes_cnt + 1)]

for _ in range(edges_cnt):
    start, end, weight = [int(x) for x in input().split()]
    graph[start].append(Edge(start, end, weight))
    graph[end].append(Edge(start, end, weight))

source = int(input())
destination = int(input())

parent = [None] * (nodes_cnt + 1)
distance = [float('inf')] * (nodes_cnt + 1)

distance[source] = 0
has_cycle = False

for node in graph:
    for edge in node:
        new_distance = distance[edge.source] + edge.weight
        if distance[edge.source] != float('inf') and new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source

for node in graph:
    for edge in node:
        new_distance = distance[edge.source] + edge.weight
        if new_distance < distance[edge.destination]:
            has_cycle = True
            break

if has_cycle:
    print("Negative Cycle Detected")
else:
    path = find_path(parent, destination, source)
    print(*path)
    print(distance[destination])
