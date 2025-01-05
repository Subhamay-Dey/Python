def solveNQueens(n):
    res = []
    board = [['.'] * n for _ in range(n)]
    
    def is_safe(row, col):

        for i in range(row):
            if board[i][col] == 'Q':
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'Q':
                return False
        return True

    def backtrack(row):
        if row == n:
            res.append(["".join(r) for r in board])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'
    
    backtrack(0)
    return res

def subsetSum(nums, target):
    res = []
    subset = []

    def backtrack(i, total):
        if total == target:
            res.append(list(subset))
            return
        if i >= len(nums) or total > target:
            return

        subset.append(nums[i])
        backtrack(i + 1, total + nums[i])
        subset.pop()

        backtrack(i + 1, total)
    
    backtrack(0, 0)
    return res

n = 8
solutions = solveNQueens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()

nums = [3, 1, 4, 2, 5]
target = 7
subset_solutions = subsetSum(nums, target)
print(subset_solutions)
