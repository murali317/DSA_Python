class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # INTUITION - 1st fill first row & first col with cumulative sum for each box. i.e., for each box, the value should be its sum + its previous box's sum (which is in DP). Now, to calculate/fill other values, add its grid value + min(top grid, left grid) and return the final grid's/box's value which finally contains the minimum path sum.
        # time - O(m*n)
        # space - O(m*n)

        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for i in range(m)]

        dp[0][0] = grid[0][0] # because this's where the path starts and this value contributes to the sum.

        for i in range(1, n):
            dp[0][i] = grid[0][i] + dp[0][i-1]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        return dp[m-1][n-1]