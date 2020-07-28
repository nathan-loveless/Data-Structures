"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        newNode = ListNode(value)
        if self.head and self.tail:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode            

        else:
            self.head = newNode
            self.tail = newNode

        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None

        else:
            value = self.head.value
            self.delete(self.head)
            return value
        

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        newNode = ListNode(value)
        
        if self.tail and self.head:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

        else:
            self.tail = newNode
            self.head = newNode
        
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail == None:
            return None
        else:
            currVal = self.tail.value
            self.delete(self.tail)
            return currVal

        self.length -= 1

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        else:
            self.delete(node)

        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node

        self.length += 1
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.tail is node:
            return self.tail
        tempVal = node.value
        self.delete(node)
        self.add_to_tail(tempVal)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head == self.tail:
            self.head = None
            self.tail = None

        elif node is self.head:
            self.head = self.head.next
            self.head.prev = None

        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        currNode = self.head
        max = self.head.value

        while currNode is not None:
            if(currNode.value > max):
                max = currNode.value
            currNode = currNode.next

        return max