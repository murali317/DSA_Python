class MinStack:
    # time - O(1) for every operation
    # space - O(n) # stack in O(n) space and for minStack - In the W.C, (descending input), every value is pushed into minStack. 
    
    def __init__(self):
        self.stack = []
        self.minStack = [] # minStack only stores a value when it is <= previous minimum. By this the min value of the input would be at top. when getMin() is called, we can return minStack[-1]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]: # do this for getMin() when needed
            self.minStack.append(val)

    def pop(self) -> None:
        if self.minStack[-1] == self.stack[-1]: # if we are popping from stack, we have to pop from minStack as well. Otherwise we may return false value through getMin() when called for the minimum value.
            self.minStack.pop()
        self.stack.pop() # I think this line is not necessary.

    def top(self) -> int:
        return self.stack[-1]
        # return self.stack[-1] if self.stack else None # just in case to handle error but this is not required because of constraints.

    def getMin(self) -> int:
        return self.minStack[-1]
        # return self.minStack[-1] if self.minStack else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()