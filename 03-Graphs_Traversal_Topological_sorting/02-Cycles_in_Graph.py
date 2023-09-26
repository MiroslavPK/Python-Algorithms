def find_node_without_dependencies(graph_dependencies):
    for node in graph_dependencies.values():
        if node == 0:
            return "Yes"
    return "No"


graph_dependencies = {}
while True:
    line = input()
    if line == 'End':
        break
    node, successor = line.split('-')

    if node not in graph_dependencies:
        graph_dependencies[node] = 0

    if successor not in graph_dependencies:
        graph_dependencies[successor] = 1
    else:
        graph_dependencies[successor] += 1

is_acyclic = find_node_without_dependencies(graph_dependencies)
print(f"Acyclic: {is_acyclic}")
