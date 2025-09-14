class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # time - O(n)
        # space - O(1)
        
        l = 0; r=0
        w_sum = 0
        min_l = float(inf)
        while r<len(nums):
            w_sum += nums[r] 
            r += 1
            while w_sum >= target: # dont use if, we still may have to check 
                min_l = min(min_l, r-l) # here r-l+1 is not necessary as we already did r+=1
                w_sum -= nums[l]
                l += 1
        return 0 if min_l == float(inf) else min_l    
