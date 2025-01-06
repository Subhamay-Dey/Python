class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to insert a node in BST
def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# Function to calculate sum of all nodes
def sum_bst(root):
    if root is None:
        return 0
    return root.val + sum_bst(root.left) + sum_bst(root.right)

# Example usage
if __name__ == "__main__":
    root = None
    values = [10, 5, 15, 3, 7, 18]
    for val in values:
        root = insert(root, val)
    
    total_sum = sum_bst(root)
    print("Sum of all nodes in BST:", total_sum)
