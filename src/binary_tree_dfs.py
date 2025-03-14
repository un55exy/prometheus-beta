class TreeNode:
    """
    Represents a node in a binary tree.
    
    Attributes:
        val (int): The value of the node
        left (TreeNode, optional): Left child node
        right (TreeNode, optional): Right child node
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_ascending_order(root):
    """
    Perform a depth-first search on a binary tree and return node values in ascending order.
    
    Args:
        root (TreeNode): The root of the binary tree
    
    Returns:
        list: A list of node values in ascending order
    
    Raises:
        TypeError: If the input is not a TreeNode or None
    """
    # Handle edge cases
    if root is None:
        return []
    
    # Validate input type
    if not isinstance(root, TreeNode):
        raise TypeError("Input must be a TreeNode or None")
    
    # Use an inorder traversal (left-root-right) to get ascending order
    def inorder_traversal(node):
        """
        Helper function to perform inorder traversal.
        
        Args:
            node (TreeNode): Current node in the traversal
        
        Returns:
            list: Node values in ascending order
        """
        if node is None:
            return []
        
        # Recursively traverse left subtree
        left_values = inorder_traversal(node.left)
        
        # Add current node's value
        current_value = [node.val]
        
        # Recursively traverse right subtree
        right_values = inorder_traversal(node.right)
        
        # Combine results
        return left_values + current_value + right_values
    
    # Return the result of inorder traversal
    return inorder_traversal(root)