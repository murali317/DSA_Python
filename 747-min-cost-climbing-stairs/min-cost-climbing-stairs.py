class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # INTUITION -> dp[i]=cost[i]+min(dp[i−1],dp[i−2]) is the base formula. Take a dp array of size n, keep filling it with current step's cost and min(previous 2 step's costs) cause this array tracks how we are paying the costs & jumping the steps until we go to the top. So when we reach the top, last 2 values of dp array holds the 2 ways of reaching the top (1. paying high amount 2. paying less amount). the min amount is the answer. (i.e. ans lies in the min(last 2 step's costs of dp array))
        # time - O(n)
        # space - O(n)

        n = len(cost)
        dp = [0] * n # O(n) space
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n): # O(n) time
            dp[i] = cost[i] + min(dp[i-1], dp[i-2]) # Each step does O(1) work → just addition + min
        return min(dp[n-1], dp[n-2])

        # Notice you only ever need the last two values (dp[i-1], dp[i-2]). so a 2 pointer approach would work and reduce the space. SPACE-OPTIMISED APPRAOCH---------
        # time - O(n)
        # space - O(1)

        n = len(cost)
        prev1 = cost[1]
        prev2 = cost[0]
        for i in range(2, n):
            res = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, res
        return min(prev1, prev2)