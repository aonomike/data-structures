from node import Node

def insert_value(root, value):
    if root is None:
        root = Node(value)
    if root.value > value:
        insert_value(root.left, value)
    elif root.value < value:
        insert_value(root.right, value)

def left_left_condition(root):
    # root->root.left->root.left.left
    new_root = root.left
    new_root.right = root
    new_root.left = root.left.left
    root = new_root

def left_right_condition(root):
    pass

def right_right_condition(root):
    pass

def right_left_condition(root):
    pass

def check_balance(root):
    if root is None:
        return -1
    if root.left and root.right:
        return calculate_height_of_node(root.left, 0) - calculate_height_of_node(root.right, 0) < 2
    if root.left is not None:
        check_balance(root.left)

    if root.right is not None:
        check_balance(root.right)



def calculate_height_of_node(root, value):
    if root is None:
        return 0
    height = 1 + value
    return max(calculate_height_of_node(root.left, height), calculate_height_of_node(root.right, height) )
    