class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


def find_path(parent, destination):
    path = []
    while destination is not None:
        path.append(destination)
        destination = parent[destination]
    return path[-1::-1]


nodes = int(input())
edges = int(input())
graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    edge = Edge(source, destination, weight)
    graph.append(edge)

start_node = int(input())
final_node = int(input())


parent = [None] * (nodes + 1)
distance = [float('inf')] * (nodes + 1)

distance[start_node] = 0

for _ in range(nodes - 1):
    for edge in graph:
        new_distance = edge.weight + distance[edge.source]
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source


for edge in graph:
    new_distance = edge.weight + distance[edge.source]
    if new_distance < distance[edge.destination]:
        print('Undefined')
        break
else:
    path = find_path(parent, final_node)
    print(*path)
    print(distance[final_node])
