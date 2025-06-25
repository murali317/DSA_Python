class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # time - O(n*k) space - O(1)
        # while val in nums: # O(n)
        #     nums.remove(val) # O(k) where val is repeated k no of times
        # return len(nums)

    # Instead of removing elements directly from the list (which is inefficient), use two pointers:
    # TIME - O(n) Space - O(1)
        i=0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j] # just replace non-val elements to front
                i+=1
        return i













