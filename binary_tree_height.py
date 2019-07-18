from node import Node

def get_height(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    return 1 + max(get_height(root.left), get_height(root.right))


node_1 = Node(3)
node_2 =  Node(1)
node_3 = Node(2)
node_4 = Node(4)

node_1.left = node_2
node_1.right = node_3
node_2.left = node_4
print(get_height(node_1))