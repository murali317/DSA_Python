class Solution:
    def rob(self, nums: List[int]) -> int:
        # INTUITION - start with nums of length = 0, 1, 2, 3, ... to get an idea. Take 2 pointers, loop form 2nd index, sum(current value+lastbefore house) compare with last house (middle wala), then shift the window forward do the same. 
        # NOTE - dp[i] = the maximum amount of money we can rob from house 0 to house i, following the rule that we can't rob two adjacent houses.
        # time - O(n)
        # space - O(1)

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # else part
        prev2, prev1 = nums[0], max(nums[0], nums[1]) # we cant rob both as they are adjacent. so the best way is to rob the higher amount
        for i in range(2, len(nums)):
            curr = max(nums[i] + prev2, prev1) # Each house is processed in constant time.
            prev2, prev1 = prev1, curr
        return curr

        # this would give O(n) space
        # dp = [0] * n
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # dp[i] = max(nums[i] + dp[i-2], dp[i-1]) 