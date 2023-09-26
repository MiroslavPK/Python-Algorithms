def find_dependencies(graph):
    dependencies = {}
    for node, children in graph.items():
        if node not in dependencies:
            dependencies[node] = 0
        for child in children:
            if child not in dependencies:
                dependencies[child] = 1
            else:
                dependencies[child] += 1
    return dependencies


def find_node_without_a_dependency(dependencies_by_node):
    for node in dependencies_by_node:
        if dependencies_by_node[node] == 0:
            return node
    return None


graph = {}
nodes = int(input())
for _ in range(nodes):
    node, children = input().split(' ->')
    graph[node] = children.strip().split(', ') if children else []

dependencies_by_node = find_dependencies(graph)

has_cycles = False
sorted_nodes = []

while dependencies_by_node:
    node_to_remove = find_node_without_a_dependency(dependencies_by_node)
    if node_to_remove is None:
        has_cycles = True
        break
    sorted_nodes.append(node_to_remove)
    dependencies_by_node.pop(node_to_remove)
    for child in graph[node_to_remove]:
        dependencies_by_node[child] -= 1

if has_cycles:
    print("Invalid topological sorting")
else:
    print(f"Topological sorting: {', '.join(sorted_nodes)}")

