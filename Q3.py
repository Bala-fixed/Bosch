class SLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLL(head):
    current = head
    while current:
        print(current.data)
        current = current.next

head = SLNode(10)
head.next = SLNode(20)
head.next.next = SLNode(30)

printLL(head)