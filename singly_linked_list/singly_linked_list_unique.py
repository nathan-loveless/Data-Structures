class Node: 
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # refference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next_node
    
    def set_next(self, new_next):
        # set this node's next node reference to the passed in node
        self.next_node = new_next

class LinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_length(self):
        return self.length

    def add_to_head(self, value):
        
        if self.contains(value) is None:
            new_node = Node(value, self.head)
            self.head = new_node

            if self.length == 0:
                self.tail = new_node

            self.length += 1
        else:
            return value

    def add_to_tail(self, value):
        if self.contains(value) is None:
            new_node = Node(value)
            if self.head is None and self.tail is None:
                self.head = new_node
            else:
                self.tail.set_next(new_node)
            self.tail = new_node
            self.length += 1

        else:
            return value
        
        

        # def check_for_duplicates(self):
        #     if self.head is None:
        #         return None
        #     else:
        #      curr_node = self.head

        #      while curr_node is not None:
        

    def get_max(self):
        if self.head is None:
            return None
        maxValue = self.head.get_value()
        currNode = self.head

        while(currNode != None):
            if(currNode.get_value() > maxValue):
                maxValue = currNode.get_value()
            currNode = currNode.get_next()
        return maxValue

    def contains(self, value):
        if self.head is None:
            return None
        
        currNode = self.head

        while currNode is not None:
            if currNode.get_value() == value:
                return value
            currNode = currNode.get_next()
        
        return None
    
    def remove_head(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()       
            return value

    def remove_tail(self):
        if self.head is None:
            return
        elif self.head == self.tail:
            currValue = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return currValue
            
        currNode = self.head

        while currNode.get_next() is not self.tail:
            currNode = currNode.get_next()

        currValue = self.tail.get_value()
        self.tail = None
        self.length -= 1
        self.tail = currNode
        return currValue


list = LinkedList()
list.add_to_tail(100)
print(f'size: {list.get_length()}')
list.add_to_tail(101)
print(f'size: {list.get_length()}')
list.add_to_tail(105)
print(f'size: {list.get_length()}')
print(f'popping 105: {list.remove_tail()}')
print(f'size: {list.get_length()}')
print(f'popping 101: {list.remove_tail()}')
print(f'size: {list.get_length()}')
print(f'popping 100: {list.remove_tail()}')
print(f'size: {list.get_length()}')
print(f'popping nothing: {list.remove_tail()}')
print(f'size: {list.get_length()}')