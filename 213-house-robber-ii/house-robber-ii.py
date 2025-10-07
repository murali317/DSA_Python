class Solution:
    def rob(self, nums: List[int]) -> int:
        # INTUITION - need to take a helper fxn to check for 2 cases: 1. include 1st house & exclude last element & get the rob amount, 2. exclude 1st house & include last house
        # time - O(n)
        # space - O(n)
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        if len(nums) == 3:
            a = max(nums[0], nums[1])
            return max(a, nums[2])

        def helper(nums):
            n = len(nums)
            dp = [0] * n
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            return dp[n-1] # last one
        
        case1 = helper(nums[:-1:]) # O(n) time
        case2 = helper(nums[1::]) # O(n) time -> O(n+n) = O(n)
        
        return max(case1, case2)