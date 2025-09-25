class Solution:
    def fib(self, n: int) -> int:
        # time - O(2^n) - Each call branches into 2 recursive calls: fib(n-1) and fib(n-2).This creates a binary tree of calls where each level doubles the number of calls (roughly). so no of call grow exponentially.
        # space - O(n) - maximum depth of the recursion stack is n
        
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

        # MEMOIZATION -----------
        # time - O(n) # Each unique value of n is computed only once and stored in memo.
        # space - O(n) - 1. memo dictionary 2. Recursion call stack

        memo = {0:0, 1:1}
        def helper(n):
            if n <= 1:
                return n
            if n in memo:
                return memo[n]
            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        return helper(n)

        # TABULATION ---------------
        # time - O(n)
        # space - O(n)

        dp = [0] * (n+1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

        # SPACE-OPTIMIZED ----------------
        # time - O(n)
        # space - O(1)

        prev1, prev2 = 1, 0
        for i in range(2, n+1):
            curr = prev1 + prev2
            prev2, prev1 = prev1, curr
        return prev1
        