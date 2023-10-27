class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


def find_root(parent, node):
    while parent[node] != node:
        node = parent[node]
    return node


nodes = int(input())
edges = int(input())
graph = []

for _ in range(edges):
    first, second, cost = [int(x) for x in input().split(' - ')]
    edge = Edge(first, second, cost)
    graph.append(edge)


parent = [idx for idx in range(nodes)]
total_cost = 0

for edge in sorted(graph, key=lambda x: x.weight):
    node_root = find_root(parent, edge.first)
    child_root = find_root(parent, edge.second)
    if node_root != child_root:
        parent[node_root] = child_root
        total_cost += edge.weight

print(f'Total cost: {total_cost}')
