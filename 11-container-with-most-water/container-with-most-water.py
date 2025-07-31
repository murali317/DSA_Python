class Solution:
    def maxArea(self, height: List[int]) -> int:
        # BRUTE FORCE (gives TLE) :- loop twice and apply area formula (length * height) but remember height should be the minimum/less of two heights (otherwise water will overflow) and distance/length should be more.
        # time - O(n^2)
        # space - O(1)
        # res = 0
        # for i in range(len(height)): # runs n times
        #     for j in range(i+1, len(height)): # runs n-i-1 times
        #         area = (j - i) * min(height[j], height[i])
        #         res = max(res, area)
        # return res

        # time - O(n)
        # space - O(1)
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            area = (r - l) * min(height[r], height[l]) # Ultimate area formula of the problem.
            res = max(res, area) # finding the max area
            # now we have to update the pointers
            if height[l] < height[r]: # we dont want the low heights 
                l += 1
            else: # if its < or =, we can move either l or r. Doesn't matter
                r -= 1
        return res