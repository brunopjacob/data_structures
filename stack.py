class Stack():

    
    """
    Stack data structure

    Attributes:
    items

    Methods:
    push(item)
    pop()
    peek()
    is_empty()
    get_stack()
    size()

    """

    
    def __init__(self):
        self.items = []
        
    def push(self,item):
        return self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def is_empty(self):
        return self.items == []
        
    def get_stack(self):
        return self.items
    
    def size(self):
        return len(self.items)
    
    

if __name__ == "__main__":

    # Create empty stack
    s = Stack()
    print(s.is_empty())

    # Add elements to stack
    s.push("A")
    s.push("B")
    s.push("C")
    
    # Peek into stack to return last element
    print(s.peek())

    # Pop last element out of the list
    s.pop()
    
    # Push new element to the list
    s.push("D")
    
    # Print elements of the stack
    print(s.get_stack())
    
