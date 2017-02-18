def get_count(node, mn, mx):
    tally = 0
    if node is not None:
        if node < mn:
            tally += get_count(node.right_child, mn, mx)
        if node > mx:
            tally += get_count(node.left_child, mn, mx)
        if node > mn and node < mx:
            tally = 1 + get_count(node.left_child, mn, mx) + get_count(node.right_child, mn, mx)
    return tally
