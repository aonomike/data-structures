class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_list(self):
        node = self
        output = ''
        while node is not None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    def reverse_iteratively(self, head):
        previous_node = None
        current_node = head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node



    def reverse_recursively(self, head, previous_node = None):
        if head == None:
            return previous_node
        current_node = head
        current_node.next_node = previous_node
        reverse_recursively(head.next, current_node)


# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail
print("Initial list: ")
print(testHead.next)
testHead.print_list()
# 4 3 2 1 0
testHead.reverse_iteratively(testHead)
#testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.print_list()
# 0 1 2 3 4
