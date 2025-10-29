# -----------------------------------------------------------------------------
# Homework 7 – MinPuzzle
# Course: CS 325 – Analysis of Algorithms
# Author: Noah Pettinato
#
# Description:
#   Solves a pathfinding puzzle by computing the minimum "effort" required
#   to move from the top-left to the bottom-right cell in a 2D grid.
#
#   The "effort" between adjacent cells is defined as the absolute difference
#   in their heights (or values). The total effort of a path is determined
#   by the maximum single-step difference along that path.
#
#   This implementation uses Dijkstra’s algorithm with a min-heap to find
#   the path minimizing maximum effort.
#
# Key Ideas:
#   • Treat each cell as a graph node connected to its 4 neighbors.
#   • Use Dijkstra’s algorithm where the edge weight is the absolute difference
#     in height between adjacent cells.
#   • Maintain a distance array that tracks the minimum effort to each cell.
#   • Time complexity: O(m * n * log(m * n))
# -----------------------------------------------------------------------------

import heapq

def minEffort(puzzle):
    """
    Compute the minimum effort required to traverse a grid from the
    top-left to the bottom-right cell.

    Parameters
    ----------
    puzzle : list[list[int]]
        2D grid of integers representing cell heights or difficulty levels.

    Returns
    -------
    int
        Minimum possible effort (defined by the largest step difference
        along the optimal path).
    """

    # Grid dimensions
    m, n = len(puzzle), len(puzzle[0])

    # Distance matrix: cumulative effort to reach each cell
    distances = [[float('inf')] * n for _ in range(m)]

    # Min-heap priority queue: (effort, row, col)
    pq = [(0, 0, 0)]
    distances[0][0] = 0

    # 4 possible movement directions: right, left, down, up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Dijkstra's algorithm
    while pq:
        cumulative_effort, row, col = heapq.heappop(pq)

        # Stop early if destination is reached
        if row == m - 1 and col == n - 1:
            return cumulative_effort

        # Explore neighboring cells
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Ensure new position is within grid bounds
            if 0 <= new_row < m and 0 <= new_col < n:
                # Effort to move to the neighbor = max(current effort, step effort)
                new_effort = max(
                    cumulative_effort,
                    abs(puzzle[new_row][new_col] - puzzle[row][col])
                )

                # Relaxation step: update if a smaller effort path is found
                if new_effort < distances[new_row][new_col]:
                    distances[new_row][new_col] = new_effort
                    heapq.heappush(pq, (new_effort, new_row, new_col))

    # Return infinity if destination is unreachable (theoretically should not happen)
    return float('inf')
