# Depth-first search
def dfs(node, explored):
    if node not in explored:
        explored.append(node)
        for neighbor in node.neighbors:
            explored = dfs(neighbor, explored)
    return explored

# Breadth-first search
def bfs(start, goal):
    explored = []
    queue = [[start]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            for neighbor in node.neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == goal:
                    return new_path
            explored.append(node)
