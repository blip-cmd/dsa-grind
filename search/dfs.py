#recursive dfs
def dfs_recursive(graph,node,visited=None, t_order=None):
    if not visited:
        visited = set()
    if not t_order:
        t_order = []
    
    visited.add(node)
    t_order.append(node)
    
    for nb in graph[node]:
        if nb not in visited:
            dfs_recursive(graph,nb,visited,t_order)
    
    return t_order

#iterative dfs (bfs twin)
def dfs(graph, start):
    visited = set()
    stack = [start] #FILO-stack instead of FIFO-queue
    t_order = []
    
    while stack:
        current = stack.pop()
        t_order.append(current)
        for nb in graph[current]:
            if nb not in visited:
                visited.add(nb)
                stack.append(nb)
    return t_order
                

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
    
    print("Graph structure:")
    for node, neighbors in graph.items():
        print(f"  {node} -> {neighbors}")
    print('dfs(graph, \'A\'):', dfs(graph, 'A'))  # Output: ['A', 'C', 'F', 'E', 'B', 'D'] (order may vary)
    print('dfs_recursive(graph, \'A\'):', dfs_recursive(graph, 'A'))  # Output: ['A', 'B', 'D', 'E', 'F', 'C'] (order may vary)