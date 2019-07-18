from node import Node

def delete_binary_tree(root):
    if root is None:
        return root
    else:
        if root.left and root.right:
            if root.left is not None:
                delete_binary_tree(root.left)
            if root.right is not None:
                delete_binary_tree(root.right)
        print('deleting root')
        root = None

node_1 = Node(3)
node_2 =  Node(1)
node_3 = Node(2)
node_4 = Node(4)

node_1.left = node_2
node_1.right = node_3
node_2.left = node_4

delete_binary_tree(node_1)
print(node_1)
