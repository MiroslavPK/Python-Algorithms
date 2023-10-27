from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


nodes = int(input())
edges = int(input())
graph = []
[graph.append([]) for _ in range(nodes)]

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split()]
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

source = int(input())
destination = int(input())

parents = [None] * nodes
reliability = [float('-inf')] * nodes

reliability[source] = 100
pq = PriorityQueue()

for _ in range(nodes):
    pq.put((-100, source))
    while not pq.empty():
        max_reliability, node = pq.get()
        if node == destination:
            break
        for edge in graph[node]:
            child = edge.second if edge.first == node else edge.first
            new_reliability = -max_reliability * edge.weight / 100
            if new_reliability > reliability[child]:
                parents[child] = node
                pq.put((-new_reliability, child))
                reliability[child] = new_reliability

path = []
node = destination

while source not in path:
    path.append(node)
    node = parents[node]

print(f'Most reliable path reliability: {reliability[destination]:.2f}%')
print(' -> '.join(str(x) for x in path[-1::-1]))
