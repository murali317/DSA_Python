class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # INTUITION - just keep checking if current element has repeated 2 spots back or not.
        # time - O(n)
        # space - O(1) - no need of using hashmap to track the count of each element, the key trick is to check if current element has repeated 2 spots back. That's it.

        i = 2
        l = len(nums)
        if l < 2:
            return l
        for j in range(2, len(nums)):
            if nums[j] != nums[i-2]:
                nums[i] = nums[j]
                i += 1
        return i