class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next 
        current.next = prev       
        prev = current            
        current = next_node
    
    return prev  

head = SinglyLinkedListNode(1)
head.next = SinglyLinkedListNode(2)
head.next.next = SinglyLinkedListNode(3)


new_head = reverse(head)

    
current = new_head
while current:
    print(current.data, end=' ')
    current = current.next