# -----------------------------------------------------------------------------
# Homework 9 – TSP
# Course: CS 325 – Analysis of Algorithms
# Author: Noah Pettinato
#
# Description:
#   Solves the Traveling Salesman Problem (TSP) using the Nearest Neighbor
#   heuristic. Starting from a fixed node (node 0), the algorithm repeatedly
#   visits the nearest unvisited neighbor until all nodes have been visited,
#   then returns to the starting node.
#
#   This heuristic does not guarantee an optimal route but is efficient
#   and often yields a good approximation for small to medium graphs.
#
# Key Ideas:
#   • Represent the graph as an adjacency matrix.
#   • Start from vertex 0 and iteratively choose the closest unvisited neighbor.
#   • Return to the starting vertex at the end to complete the cycle.
#   • Time complexity: O(n²)
# -----------------------------------------------------------------------------

def solve_tsp(G):
    """
    Solve the Traveling Salesman Problem using the Nearest Neighbor heuristic.

    Parameters
    ----------
    G : list[list[float]]
        Weighted adjacency matrix of the graph.
        G[i][j] = distance from vertex i to vertex j (0 if no direct edge).

    Returns
    -------
    list[int]
        Approximate TSP route as an ordered list of vertex indices,
        starting and ending at vertex 0.
    """
    num_nodes = len(G)
    path = [0]         # Start at vertex 0
    visited = {0}      # Track visited vertices

    # Greedily visit the nearest unvisited node
    while len(visited) < num_nodes:
        current_node = path[-1]
        min_distance = float('inf')
        nearest_neighbor = None

        # Find nearest unvisited neighbor
        for neighbor, distance in enumerate(G[current_node]):
            if distance > 0 and neighbor not in visited and distance < min_distance:
                min_distance = distance
                nearest_neighbor = neighbor

        # Move to the selected neighbor
        path.append(nearest_neighbor)
        visited.add(nearest_neighbor)

    # Return to the starting node to complete the cycle
    path.append(0)
    return path
