import heapq
from collections import defaultdict

def quantum_chessboard_path(board, initial_energy):
    N = len(board)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    
    # Locate all portals on the board
    portals = defaultdict(list)
    for i in range(N):
        for j in range(N):
            if board[i][j] == -1:
                portals[-1].append((i, j))

    # Priority queue for Dijkstra's algorithm
    pq = [(0, initial_energy, 0, 0, [(0, 0)])]  # (energy used, remaining energy, x, y, path)
    visited = {}

    while pq:
        energy_used, energy_left, x, y, path = heapq.heappop(pq)

        # If we reached the target, return the result
        if (x, y) == (N - 1, N - 1):
            return (energy_used, path)

        # If already visited with more energy left, skip
        if (x, y) in visited and visited[(x, y)] >= energy_left:
            continue
        visited[(x, y)] = energy_left

        # Explore all four possible moves
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                cell_value = board[nx][ny]
                new_energy_used = energy_used + cell_value
                new_energy_left = energy_left - cell_value

                # If we have enough energy to move to this cell
                if new_energy_left >= 0:
                    heapq.heappush(pq, (new_energy_used, new_energy_left, nx, ny, path + [(nx, ny)]))

        # Check if we're on a portal, and teleport if so
        if board[x][y] == -1:
            for px, py in portals[-1]:
                if (px, py) != (x, y):  # Teleport to a different portal
                    heapq.heappush(pq, (energy_used, energy_left, px, py, path + [(px, py)]))
            
            # Remove the portal after usage to ensure it's used only once
            portals[-1] = [p for p in portals[-1] if p != (x, y)]

    # If we exhaust all options without reaching the target
    return -1

# Example usage
board = [
    [1, -1, 5],
    [3, 10, -1],
    [1, 1, 1]
]
initial_energy = 10
result = quantum_chessboard_path(board, initial_energy)
print(result)  # Expected output: (6, [(0,0), (1,0), (2,0), (2,1), (2,2)])
