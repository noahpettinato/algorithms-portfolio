# -----------------------------------------------------------------------------
# Homework 8 – Puzzle
# Course: CS 325 – Analysis of Algorithms
# Author: Noah Pettinato
#
# Description:
#   Solves a grid-based puzzle by representing open cells as graph nodes
#   and applying Breadth-First Search (BFS) to find a path from a source
#   cell to a destination cell.
#
#   Each move between adjacent open cells (denoted by '-') is treated as an
#   edge in the graph. The output includes both the sequence of coordinates
#   visited and the corresponding move directions (U, D, L, R).
#
# Key Ideas:
#   • Represent the grid as an adjacency list.
#   • Use BFS for shortest-path discovery in an unweighted grid.
#   • Track both cell coordinates and movement directions.
#   • Time complexity: O(m * n)
# -----------------------------------------------------------------------------

def create_graph(puzzle):
    """
    Construct an adjacency list representation of the grid.

    Parameters
    ----------
    puzzle : list[list[str]]
        2D grid where '-' indicates an open cell and other symbols represent walls.

    Returns
    -------
    dict
        Graph representation where keys are coordinates (i, j) and
        values are lists of (neighbor_coordinate, direction) tuples.
    """
    graph = {}
    directions = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]

    for i, row in enumerate(puzzle):
        for j, cell in enumerate(row):
            if cell == '-':
                graph[(i, j)] = []
                for dr, dc, label in directions:
                    x, y = i + dr, j + dc
                    # Check if neighbor is within bounds and open
                    if 0 <= x < len(puzzle) and 0 <= y < len(puzzle[0]) and puzzle[x][y] == '-':
                        graph[(i, j)].append(((x, y), label))
    return graph


def solve_puzzle(puzzle, source, destination):
    """
    Solve the grid puzzle using BFS to find a path between source and destination.

    Parameters
    ----------
    puzzle : list[list[str]]
        2D grid representation.
    source : tuple[int, int]
        Starting coordinate (row, col).
    destination : tuple[int, int]
        Target coordinate (row, col).

    Returns
    -------
    tuple[list[tuple[int, int]], str] or None
        Path as a list of coordinates and corresponding direction string,
        or None if no path exists.
    """
    graph = create_graph(puzzle)
    queue = [(source, [source], '')]  # Each element: (current_node, path_so_far, directions_string)
    visited = set()

    while queue:
        node, path, directions_str = queue.pop(0)
        visited.add(node)

        # If destination reached, return full path and movement sequence
        if node == destination:
            return path, directions_str

        # Explore neighbors
        for neighbor, direction in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor], directions_str + direction))

    # If destination is unreachable
    return None
