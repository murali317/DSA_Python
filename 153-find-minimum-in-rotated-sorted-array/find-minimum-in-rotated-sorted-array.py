class Solution:
    def findMin(self, nums: List[int]) -> int:
        # INTUITION - In a rotated sorted array (with no duplicates), the smallest element is the only one where: nums[i] < nums[i - 1] and comparing mid value with right value is enough to figure out in which half the minimum value lies. take an example and dry run to get this intuition.
        # time - O(log n)
        # space - O(1)

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]: 
                left = mid + 1
            elif nums[mid] <= nums[right]:
                right = mid
        return nums[left]
        
