from node import Node

def sum_all_numbers_from_root_to_leaf(root, value):
    if root is None:
        return 0
    sum = value * 10 + root.value
    if root.left is None and root.right is None:
        return sum

    return (sum_all_numbers_from_root_to_leaf(root.left, sum) + \
        sum_all_numbers_from_root_to_leaf(root.right, sum))

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

print(sum_all_numbers_from_root_to_leaf(node_1, 0))
