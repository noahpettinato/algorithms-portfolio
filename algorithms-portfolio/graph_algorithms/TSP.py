def solve_tsp(G):
    num_nodes = len(G)
    path = [0]
    visited = {0}
    while len(visited) < num_nodes:
        current_node = path[-1]
        min_distance = float('inf')
        nearest_neighbor = None
        for neighbor, distance in enumerate(G[current_node]):
            if distance > 0 and neighbor not in visited and distance < min_distance:
                min_distance = distance
                nearest_neighbor = neighbor
        path.append(nearest_neighbor)
        visited.add(nearest_neighbor)
    path.append(0)
    return path