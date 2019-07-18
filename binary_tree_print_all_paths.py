from node import Node

def print_all_paths_from_root(root, path):
    if root is None:
        return None
    path = path + str(root.value)
    if root.left is None and root.right is None:
        print(path)
        return path
    print_all_paths_from_root(root.left, path)
    print_all_paths_from_root(root.right, path)
    
node_1 = Node(3)
node_2 =  Node(1)
node_3 = Node(2)
node_4 = Node(4)
node_5 = Node(5)
node_6 = Node(6)
node_7 = Node(7)

node_1.left = node_2
node_1.right = node_3
node_2.left = node_4
node_2.right = node_5
node_5.left = node_6
node_2.left = node_7

print(print_all_paths_from_root(node_1, ''))
