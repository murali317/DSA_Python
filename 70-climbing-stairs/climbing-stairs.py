class Solution:
    def climbStairs(self, n: int) -> int:
        # INTUITION - If you are at step i, you could have come from step i-1 by taking 1 step, or from step i-2 by taking 2 steps. i.e., ways(i) = ways(i-1) + ways(i-2)
        # time - O(n)
        # space - O(n)
        dp = [0] * (n + 1)
        dp[0] = 1 # There's one way to stay at step 0 (do nothing)
        dp[1] = 1 # There's one way to reach step 1 (one 1-step move/single step)
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]