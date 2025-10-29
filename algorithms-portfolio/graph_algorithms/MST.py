import heapq
def Prims(G):
    n = len(G)
    visited = [False] * n
    min_heap = []
    mst_edges = []
    # Start from vertex 0
    visited[0] = True
    for j in range(n):
        if G[0][j] != 0:
            heapq.heappush(min_heap, (G[0][j], 0, j))
    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        if not visited[v]:
            visited[v] = True
            mst_edges.append((u, v, weight))
            for j in range(n):
                if G[v][j] != 0 and not visited[j]:
                    heapq.heappush(min_heap, (G[v][j], v, j))
    return mst_edges