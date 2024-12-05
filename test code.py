class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None        
    def __str__(self):
        return str(self.data)
class LinkedList:
    def __init__(self):
        # Initialize the head of
        # the list as None
        self.head = None
    def append(self, data):
        # Create a new node with the given data
        new_node = Node(data)  
        if self.head is None:
            # If the list is empty, set the 
            # new node as the head
            self.head = new_node 
        else:
            # Traverse to the end of 
            # the list
            current = self.head
            while current.next:  
                current = current.next
            # Link the last node to 
            # the new node
            current.next = new_node
    def traverse(self):
        current = self.head
        # Traverse the list and
        # print each node's data
        while current:  
            print(current.data,
                  end=" -> ")
            current = current.next
        print("None")
# driver code
ll = LinkedList()
for i in range(10):
    ll.append(i)    
ll.traverse()
