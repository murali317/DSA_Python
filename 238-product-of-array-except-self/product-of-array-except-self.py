class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # INTUITION - Take an output array & a prefix = 1 -> as we iterate in nums, for the left side of each index, store it in output[i] and consecutively mulitply prefix with nums[i]. Similarly, take a postfix = 1 -> as we iterate from the end, for the right side of each index, store (postfix * output[i]) in output[i] and consecutively mulitply postfix with nums[i].
        # time - O(n) - for looping
        # space - O(1)

        output = [1] * len(nums) # O(1) space as mentioned in problem
        
        prefix = 1 # prod of all left side elements of current index
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        postfix = 1 # prod of all right side elements of current index
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return output

