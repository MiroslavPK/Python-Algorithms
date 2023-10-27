class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


def find_root(parent, node):
    while parent[node] != node:
        node = parent[node]
    return node


edges_cnt = int(input())
graph = []
parent = []
max_node = -1

for _ in range(edges_cnt):
    source, destination, weight = [int(x) for x in input().split(', ')]
    graph.append(Edge(source, destination, weight))
    max_node = max(source, destination, max_node)

parent = [idx for idx in range(max_node + 1)]

for edge in sorted(graph, key=lambda x: x.weight):
    source_root = find_root(parent, edge.source)
    destination_root = find_root(parent, edge.destination)
    if source_root != destination_root:
        print(f"{edge.source} - {edge.destination}")
        parent[source_root] = destination_root

