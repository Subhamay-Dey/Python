class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longest_path(root):
    # Variable to store the maximum path length
    max_path_length = 0

    def dfs(node):
        nonlocal max_path_length
        if not node:
            return 0

        # Recursively find the depth of left and right subtrees
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)

        # Update the maximum path length if the current path is longer
        max_path_length = max(max_path_length, left_depth + right_depth)

        # Return the height of the current subtree
        return max(left_depth, right_depth) + 1

    dfs(root)
    return max_path_length

# Example Usage
if __name__ == "__main__":
    # Construct the example tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Longest Path Length:", longest_path(root))  # Output: 3
