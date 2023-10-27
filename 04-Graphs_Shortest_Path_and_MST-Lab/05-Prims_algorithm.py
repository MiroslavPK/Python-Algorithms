from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __gt__(self, other):
        return self.weight > other.weight


def prim(node, graph, forest):
    forest.add(node)
    pq = PriorityQueue()

    for edge in graph[node]:
        pq.put(edge)

    while not pq.empty():
        non_tree_node = -1
        min_edge = pq.get()

        if min_edge.first in forest and min_edge.second not in forest:
            non_tree_node = min_edge.second
        elif min_edge.first not in forest and min_edge.second in forest:
            non_tree_node = min_edge.first

        if non_tree_node == -1:
            continue

        print(f'{min_edge.first} - {min_edge.second}')

        forest.add(non_tree_node)

        for edge in graph[non_tree_node]:
            pq.put(edge)


edges_cnt = int(input())
graph = {}

for _ in range(edges_cnt):
    first, second, weight = [int(x) for x in input().split(", ")]
    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

forest = set()

for node in graph:
    prim(node, graph, forest)
