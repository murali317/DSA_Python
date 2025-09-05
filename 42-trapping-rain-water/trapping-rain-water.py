class Solution:
    def trap(self, height: List[int]) -> int:
        # INTUITION - min(left_max_val, right_max_val) - height[i] is the core intuition at each step as we loop, and then return the final result. Followed the 2-pointer approach for O(1) memory. Otherwise stack would be O(n) memory.
        # time - O(n) # Travesing with 2 pointers moving atmost n steps in total. Each element is visited only once.
        # space - O(1)

        if len(height) == 1:
            return 0
        res = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r] # store the leftmax & rightmax values
        while l < r:
            if leftMax < rightMax: 
                l += 1 # move l if this satisfies.
                leftMax = max(leftMax, height[l]) # have to update max_left_value at each step
                res += leftMax - height[l] # Add the values at each step to res.
            else: 
                r -= 1 # else move r
                rightMax = max(rightMax, height[r]) # have to update max_right_value at each step
                res += rightMax - height[r] # Add the values at each step to res.
        return res
                