from queue import PriorityQueue


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight


def dijkstra(graph, start_node, destination_node):
    pq.put((0, start_node))
    while not pq.empty():
        min_distance, node = pq.get()
        if node == destination_node:
            break
        for edge in graph[node]:
            new_distance = min_distance + edge.weight
            if new_distance < distance[edge.end]:
                parent[edge.end] = node
                distance[edge.end] = new_distance
                pq.put((new_distance, edge.end))


def find_path(parent, start_node, destination_node):
    path = [destination_node]
    while True:
        destination_node = parent[destination_node]
        path.append(destination_node)
        if destination_node == start_node:
            break
    return list(reversed(path))


edges_cnt = int(input())
graph = {}

for _ in range(edges_cnt):
    start, end, weight = [int(inp) for inp in input().split(", ")]
    if start not in graph:
        graph[start] = []
    if end not in graph:
        graph[end] = []
    graph[start].append(Edge(start, end, weight))

start_node = int(input())
destination_node = int(input())


max_node = max(graph.keys())
parent = [None] * (max_node + 1)
distance = [float('inf')] * (max_node + 1)

distance[start_node] = 0
pq = PriorityQueue()

dijkstra(graph, start_node, destination_node)

if distance[destination_node] == float('inf'):
    print("There is no such path.")
else:
    path = find_path(parent, start_node, destination_node)
    print(distance[destination_node])
    print(*path) 
