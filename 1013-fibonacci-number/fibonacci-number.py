class Solution:
    def fib(self, n: int) -> int:
        # time - O(2^n) - Each call branches into 2 recursive calls: fib(n-1) and fib(n-2).This creates a binary tree of calls where each level doubles the number of calls (roughly). so no of call grow exponentially.
        # space - O(n) - maximum depth of the recursion stack is n
        
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
        