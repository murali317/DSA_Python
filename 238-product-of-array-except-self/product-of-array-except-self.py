class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # INTUITION - Take an output array & a prefix = 1 -> as we iterate in nums, for the left side of each index, store it in output[i] and consecutively mulitply prefix with nums[i]. Similarly, take a postfix = 1 -> as we iterate from the end, for the right side of each index, store (postfix * output[i]) in output[i] and consecutively mulitply postfix with nums[i].

        # time - O(n)
        # space - O(n)
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(n):
            result[i] = prefix[i] * suffix[i]

        return result

# ---------------------------------------------------------------------

        # time - O(n)
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
