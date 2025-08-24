class Stack:
    def __init__(self):
        self.stack = []   # Empty list 

    # Push operation 
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to stack")

    # Pop operation 
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty! Cannot Pop")
        else:
            removed = self.stack.pop()
            print(f"Popped {removed} from stack")

    # Peek operation 
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty! Nothing to Peek")
        else:
            print(f"Top element is {self.stack[-1]}")

    # isEmpty operation 
    def isEmpty(self):
        return len(self.stack) == 0

# --------- Test ---------
s = Stack()
s.push(10)   # Insert 10
s.push(20)   # Insert 20
s.peek()     # Show top element
s.pop()      # Remove top element
s.peek()     # Show top element
