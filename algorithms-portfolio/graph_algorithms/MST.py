# -----------------------------------------------------------------------------
# Homework 8 – MST
# Course: CS 325 – Analysis of Algorithms
# Author: Noah Pettinato
#
# Description:
#   Computes the Minimum Spanning Tree (MST) of a weighted, undirected graph
#   using Prim’s algorithm and a min-heap (priority queue).
#
#   The MST is a subset of edges that connects all vertices together
#   without any cycles and with the minimum possible total edge weight.
#
# Key Ideas:
#   • Start from an arbitrary vertex (vertex 0 here).
#   • Use a priority queue to repeatedly select the smallest edge
#     connecting a visited vertex to an unvisited vertex.
#   • Continue until all vertices are included in the MST.
#   • Time complexity: O(E log V)
# -----------------------------------------------------------------------------

import heapq

def Prims(G):
    """
    Compute the Minimum Spanning Tree (MST) using Prim’s algorithm.

    Parameters
    ----------
    G : list[list[int]]
        Weighted adjacency matrix of the graph.
        G[i][j] = 0 means no edge between vertices i and j.

    Returns
    -------
    list[tuple[int, int, int]]
        List of edges (u, v, weight) included in the MST.
    """

    n = len(G)                   # Number of vertices
    visited = [False] * n        # Track visited vertices
    min_heap = []                # Priority queue for edges
    mst_edges = []               # Store edges in the MST

    # Start from vertex 0
    visited[0] = True
    for j in range(n):
        if G[0][j] != 0:
            heapq.heappush(min_heap, (G[0][j], 0, j))

    # Main loop: extract minimum weight edge until MST is complete
    while min_heap:
        weight, u, v = heapq.heappop(min_heap)

        # Skip if vertex v is already in MST
        if not visited[v]:
            visited[v] = True
            mst_edges.append((u, v, weight))

            # Add all edges from v to unvisited vertices
            for j in range(n):
                if G[v][j] != 0 and not visited[j]:
                    heapq.heappush(min_heap, (G[v][j], v, j))

    return mst_edges
