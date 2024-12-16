def max_path_sum(grid):
    rows, cols = len(grid), len(grid[0])
    
    # Initialize the DP table with -infinity
    dp = [[float('-inf')] * cols for _ in range(rows)]
    dp[0][0] = grid[0][0]  # Start at the top-left cell

    # Fill the DP table
    for i in range(rows):
        for j in range(cols):
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + grid[i][j])  # From top
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1] + grid[i][j])  # From left
            if i > 0 and j > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + grid[i][j])  # From diagonal

    # The bottom-right cell contains the maximum path sum
    return dp[-1][-1]


# Test case
grid = [
    [5, 3, -1],
    [2, -4, 6],
    [1, -1, 2]
]
print(max_path_sum(grid))  # Output: 15
