class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # BRUTE FORCE - TLE ❌
        # time - O(n^2)
        # space - O(1)
        # max_sum = float('-inf')
        # for i in range(len(nums)):
        #     curr_sum = 0
        #     for j in range(i, len(nums)):
        #         curr_sum += nums[j]
        #         if curr_sum > max_sum:
        #             max_sum = curr_sum
        # return max_sum

        # KADANE'S ALGORITHM
        # time - O(n)
        # space - O(1)
        ms = float('-inf')
        cs = 0
        for i in nums:
            if cs < 0:
                cs = 0
            cs += i
            ms = max(ms, cs)
        return ms