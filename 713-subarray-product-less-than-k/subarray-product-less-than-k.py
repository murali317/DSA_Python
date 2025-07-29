class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # INTUITION - sliding window is perfect for this. Think to grow the window and keep counting no of valid subarrays in btw & shrink the window while removing first element of the window by dividing it from the entire prod of that subarray, then move forward. Finally to count -> add (right - left + 1) while expanding.
        # ✅ Always remember to use this math trick (r-l+1) to count subarrays
        # ✅ for contiguous subarray problems, think SLIDING WINDOW
        
        # time - O(n) In total each pointer moves atmost 0 -> n-1 steps. 
        # space - O(1)

        i = 0; j = 0
        prod = 1
        count = 0
        while j<len(nums):
            prod *= nums[j]
            while prod >= k and i<=j: # not extra O(n) cause it just increments
                prod //= nums[i]
                i += 1
            count += j - i + 1 # observe this, have to think like this, not always count += 1.
            j += 1
        return count