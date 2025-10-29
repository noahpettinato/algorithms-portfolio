import heapq

def minEffort(puzzle):
    # Get dimensions of the puzzle
    m, n = len(puzzle), len(puzzle[0])
    # Initialize distance array to store cumulative effort required to reach each cell
    distances = [[float('inf')] * n for _ in range(m)]
    # Initialize priority queue for Dijkstra's algorithm
    pq = [(0, 0, 0)]  # (cumulative effort, row, column)
    distances[0][0] = 0
    # Define directions: right, left, down, up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # Dijkstra's algorithm
    while pq:
        cumulative_effort, row, col = heapq.heappop(pq)
        # Check if the current cell is the destination
        if row == m - 1 and col == n - 1:
            return cumulative_effort
        # Explore neighboring cells
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            # Check if neighboring cell is within bounds
            if 0 <= new_row < m and 0 <= new_col < n:
                # Calculate effort required to move to the neighboring cell
                new_effort = max(cumulative_effort, abs(puzzle[new_row][new_col] - puzzle[row][col]))
                # Update cumulative effort if new effort is less than current effort
                if new_effort < distances[new_row][new_col]:
                    distances[new_row][new_col] = new_effort
                    heapq.heappush(pq, (new_effort, new_row, new_col))
    # If destination cell is unreachable, return infinity
    return float('inf')