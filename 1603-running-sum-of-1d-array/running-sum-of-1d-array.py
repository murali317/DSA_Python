class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # time - O(n^2) 
        # space - O(n)
        # arr = []
        # for i in range(len(nums)):
        #     arr.append(sum(nums[:i+1]))
        # return arr

        # INTUITION - keep summing it cumulatively and do inplace modification
        # time - O(n)
        # space - O(1)
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums

        # ALTERNATE APPRAOCH
        # time - O(n)
        # space - O(1)
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            nums[i] = total
        return nums