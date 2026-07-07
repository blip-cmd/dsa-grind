def bfs(graph, start):
    visited = set([start])
    queue = [start]
    traversal_order = []
    while queue:
        current = queue.pop(0)
        traversal_order.append(current)
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal_order

# Example use:
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print(bfs(graph, 'A'))  # Output: ['A', 'B', 'C', 'D', 'E', 'F']