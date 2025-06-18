from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # think that as the sliding window is moving forward, we need to remove elements from the front and also add from the back which is why we should use a "QUEUE"
        l, r, output = 0, 0, []
        q = deque() # Will store indices of potential max values
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r) # storing the indices, not the values
            
            if l > q[0]:
                q.popleft()
            
            # If window has hit size k, add max to output
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output


            
        




