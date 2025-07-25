def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Use a set to keep track of visited nodes

    visited.add(start)
    print(start, end=' ')  # Visit the node (print it)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Traversal starting from node A:")
dfs(graph, 'A')
