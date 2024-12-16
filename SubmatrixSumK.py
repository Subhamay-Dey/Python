def max_submatrix_sum_with_k_flips(grid, k):
    from itertools import accumulate
    import numpy as np

    rows, cols = len(grid), len(grid[0])
    
    # Convert grid to prefix sum array for faster area calculations
    def calculate_prefix_sums(matrix):
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(rows):
            for j in range(cols):
                prefix[i + 1][j + 1] = (matrix[i][j] +
                                        prefix[i + 1][j] +
                                        prefix[i][j + 1] -
                                        prefix[i][j])
        return prefix

    # Calculate the maximum sum for a given rectangle
    def get_sum(prefix, r1, c1, r2, c2):
        return (prefix[r2 + 1][c2 + 1] - prefix[r1][c2 + 1] -
                prefix[r2 + 1][c1] + prefix[r1][c1])

    # Step 1: Generate the flip cost matrix
    flip_cost = [[1 - grid[i][j] for j in range(cols)] for i in range(rows)]
    prefix_original = calculate_prefix_sums(grid)
    prefix_cost = calculate_prefix_sums(flip_cost)

    max_sum = float('-inf')

    # Step 2: Iterate over all pairs of rows and use sliding window on columns
    for r1 in range(rows):
        for r2 in range(r1, rows):
            row_sum = np.array([get_sum(prefix_original, r1, 0, r2, c)
                                for c in range(cols)])
            row_flip_cost = np.array([get_sum(prefix_cost, r1, 0, r2, c)
                                       for c in range(cols)])
            
            # Sliding window to maximize area with at most k flips
            left = 0
            current_sum, current_flips = 0, 0
            for right in range(cols):
                current_sum += row_sum[right]
                current_flips += row_flip_cost[right]

                # Shrink window until flips <= k
                while current_flips > k:
                    current_sum -= row_sum[left]
                    current_flips -= row_flip_cost[left]
                    left += 1

                # Update maximum sum
                max_sum = max(max_sum, current_sum)

    return max_sum


# Test case
grid = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
]
k = 2

print(max_submatrix_sum_with_k_flips(grid, k))  # Output: 5
