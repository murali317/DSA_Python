class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # time - O(n^2) 
        # space - O(n)
        # arr = []
        # for i in range(len(nums)):
        #     arr.append(sum(nums[:i+1]))
        # return arr

        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums