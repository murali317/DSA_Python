class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # INTUITION - First, take a 2D array and fill with zeroes, then fill the first row & first column with ones as no of paths to reach those boxes/places is only 1. but for diagonal/remaining places, dp[i][j] = dp[i-1][j] + dp[i][j-1] is the formula. 
        # time - O(m*n) - the outer loop runs m times, and inner loop runs n times.
        # space - O(m*n) m x n DP table

        dp = [[0] * n for i in range(m)] # O(m*n) space
        for i in range(n):
            dp[0][i] = 1
        for j in range(m):
            dp[j][0] = 1
        
        for i in range(1, m): # O(m*n) time 
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1] # the last box