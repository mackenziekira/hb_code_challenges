def height_bt(node):
    """returns the heigt of a binary tree"""

    if not node:
        return 0

    left_height = 1 + height_bt(node.left)
    right_height = 1 + height_bt(node.right)
    
    return max(left_height, right_height)