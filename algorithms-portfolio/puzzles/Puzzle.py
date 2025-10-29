def create_graph(puzzle):
    graph = {}
    directions = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]
    for i, row in enumerate(puzzle):
        for j, cell in enumerate(row):
            if cell == '-':
                graph[(i, j)] = []
                for d in directions:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < len(puzzle) and 0 <= y < len(puzzle[0]) and puzzle[x][y] == '-':
                        graph[(i, j)].append(((x, y), d[2]))
    return graph
def solve_puzzle(puzzle, source, destination):
    graph = create_graph(puzzle)
    queue = [(source, [source], '')]
    visited = set()
    while queue:
        node, path, directions_str = queue.pop(0)
        visited.add(node)
        if node == destination:
            return path, directions_str
        for neighbor, direction in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor], directions_str + direction))
    return None