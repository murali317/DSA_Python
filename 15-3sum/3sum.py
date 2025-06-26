class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # time - O(n^2) space - O(N)
        nums.sort() # O(n log n)
        res = [] # O(n) for storing triplets in worst case
        for i,j in enumerate(nums): # O(n)
            if i > 0 and j == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r: # O(n)
                three_sum = j + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([j, nums[l],  nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
