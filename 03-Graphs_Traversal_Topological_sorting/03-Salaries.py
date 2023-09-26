def dfs(hierarchy, node, visited, salaries_book):
    if visited[node]:
        return
    visited[node] = True
    successors = hierarchy[node]
    if 'Y' not in successors:
        salaries_book[node] = 1
    else:
        for i in range(len(successors)):
            if successors[i] == 'Y':
                dfs(hierarchy, i, visited, salaries_book)
                if node not in salaries_book:
                    salaries_book[node] = 0
                salaries_book[node] += salaries_book[i]
    return salaries_book


employees = int(input())
hierarchy = []
salaries_book = {}

for employee in range(employees):
    hierarchy.append(list(input()))

visited = [False] * len(hierarchy)

if employees == 1:
    salaries_book[0] = employees
else:
    for node in range(employees):
        if visited[node]:
            continue
        salaries_book = dfs(hierarchy, node, visited, salaries_book)

print(sum(salaries_book.values()))
