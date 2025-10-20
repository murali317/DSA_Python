class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # INTUITION - Be aware with the edge cases and find them at start.
        # time - O(m*n)
        # space - O(m*n)

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If start or end is blocked, return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        # DP table initialization
        dp = [[0] * n for i in range(m)]
        
        # Start position is 1 assuming no obstacle there
        dp[0][0] = 1

        for i in range(1, n): 
            if obstacleGrid[0][i] == 1:
                break # no going further, break the loop and continue with next one
            dp[0][i] = dp[0][i-1] # this skips the start position
        for i in range(1, m): 
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = dp[i-1][0] # this also skips the start position so we assigned dp[0][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0 # No paths through obstacles
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1] # since its a mxn so dont do dp[m-1][m-1] thinking it is mxm or similarly as nxn