class MyStack:
    # INTUITION - We have to make the newest pushed ele always at the front of q1 so we can pop directly from front. for that we shouldn't use pop(). So we can have 2 queues in which second queue can be used to first hold the added ele, append the 1st Q's elements to it (it will be in our disired order now but those would in Q2), so now we swap Q1 & Q2, then return Q1. Q2 will act as a Mother providing food to her son (Q1).
    # time - O(n)
    # space - O(n)

    from collections import deque
    def __init__(self):
        self.queue1 = deque()   
        self.queue2 = deque()

    def push(self, x: int) -> None: # O(n)
        self.queue2.append(x)
        while self.queue1: # O(n) time
            self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int: # O(1)
        return self.queue1.popleft()

    def top(self) -> int: #O(1)
        return self.queue1[0]

    def empty(self) -> bool: #O(1)
        return not self.queue1 and not self.queue2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()