class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def is_identical(root_1, root_2):
    if root_1 is None and root_2 is None:
        return True
    if (root_1 is not None and root_2 is not None) and (root_1.value == root_2.value):
        return is_identical(root_1.left, root_2.left) and \
        is_identical(root_1.right, root_2.right)
        
    else:
        return False

def is_identical_iterative(node_1, node_2):
    if node_1 is None and node_2 is None:
        return True
    elif node_1 is None and node_2 is not None or node_1 is not None and node_2 is None:
        return False

    arr = [[node_1, node_2]]
    while arr.__len__() > 0:
        node_array  = arr.pop(0)
        node1 = node_array.pop()
        node2 = node_array.pop()
        
        if not (node1 and node2) and (node1.value == node2.value):
            return False
        if node1.left and node2.left:
            arr.append([node1.left, node2.left])
        elif node1.left or node2.left:
            return False
        if node1.right and node2.right:
            arr.append([node1.right, node2.right])
        elif node1.right or node2.right:
            return False
    return True

node_1 = BinaryNode(3)
node_2 =  BinaryNode(1)
node_3 = BinaryNode(2)
node_4 =  BinaryNode(3)
node_5 = BinaryNode(2)
node_6 =  BinaryNode(2)

node_1.left = node_2
node_1.right = node_3
node_4.left = node_5
node_4.right = node_6 

print(is_identical(node_1, node_4))
print(is_identical_iterative(node_1, node_4))