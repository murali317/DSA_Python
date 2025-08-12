class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # INTUITION - use binary search by starting low = 1 and high = max(piles). Then keep increasing/decreasing mid value upon comparing with 'h'.
        
        # time - O(n log n)
        # space - O(1)

        import math
        low = 1
        high = max(piles) # O(n)
        count = 0
        while low < high:
            mid = (low + high) // 2 
            count = sum(math.ceil(i/mid) for i in piles) # Count needs to represent only this iteration’s total hours — not a running total (so its not count +=).
            if count <= h:
                high = mid
            else:
                low = mid + 1
        return high # take an example and check. dont return count.