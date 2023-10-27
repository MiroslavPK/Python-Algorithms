from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight, connected):
        self.first = first
        self.second = second
        self.weight = weight
        self.connected = connected

    def __gt__(self, other):
        return self.weight > other.weight


def prim(graph, network, budget):
    while not pq.empty():
        non_tree_node = -1
        min_edge = pq.get()
        if min_edge.weight <= budget:
            if min_edge.first in network and min_edge.second not in network:
                non_tree_node = min_edge.second
            if min_edge.first not in network and min_edge.second in network:
                non_tree_node = min_edge.first

            if non_tree_node == -1:
                continue

            network.add(non_tree_node)
            for edge in graph[non_tree_node]:
                pq.put(edge)

        return min_edge.weight
    return -1


initial_budget = int(input())
nodes = int(input())
edges = int(input())

graph = {}
network = set()
pq = PriorityQueue()

for _ in range(edges):
    args = input().split()
    first, second, weight = [int(x) for x in args[:3]]
    connected = True if len(args) == 4 else False

    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []

    edge = Edge(first, second, weight, connected)
    graph[first].append(edge)
    graph[second].append(edge)

    if connected:
        network.add(first)
        network.add(second)
    else:
        pq.put(edge)


budget_left = initial_budget
for node in graph:
    current_weight = prim(graph, network, budget_left)
    if current_weight == -1 or current_weight > budget_left:
        break
    budget_left -= current_weight

print(f'Budget used: {initial_budget - budget_left}')
