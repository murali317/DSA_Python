class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # time - O(n^2)
        # space - O(1)
        # for i in nums:
        #     if i==0: 
        #         nums.remove(i) # O(n)
        #         nums.append(i) # O(1)
        

        # INTUITION - we should move non zeroes to the left of the array so swap.
        # time - O(n) space - O(1)
        ins = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[ins] = nums[ins], nums[i]
                ins += 1