class MyQueue:
    # time - O(n) space - O(n) 
    # Amortized - O(1) time.
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)        

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2




#     from collections import deque
#     def __init__(self):
#         self.queue = []
#         # self.queue = deque()

#     def push(self, x: int) -> None:
#         self.queue.append(x)
#         # self.queue.append(x)

#     def pop(self) -> int:
#         return self.queue.pop(0) # The pop(0) operation has a time complexity of O(n) because it requires shifting all subsequent elements one position to the left.
# # For small queues or scenarios with infrequent pop operations, this is fine, but for large queues or performance-critical applications, this can become a bottleneck.

# # so in the description, they mentioned AMORTIZED O(1) that means taking 2-stack implementation in action.
# # Slightly more complex than this but highly efficient for Larger queues 
#         # return self.queue.popleft()

#     def peek(self) -> int:
#         return self.queue[0]
#         # return self.queue[0]

#     def empty(self) -> bool:
#         return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()