class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # INTUITION - unlike 2sum, no need of hashmap here as we have to output elements directly, not its indices. so take 2 pointers l & r at 2nd position and last positions. keep checking those 2 pointers with first element. dont forget to skip duplicates by checking if current element (l) == previous element (nums[l-1]).
        # time - O(n^2)
        # space - O(n)
        
        nums.sort() # O(n log n)
        res = [] # O(n) for storing triplets in worst case
        for i,j in enumerate(nums): # O(n)
            if i > 0 and j == nums[i-1]: #l this is for the outer loop, not inner loop (not inner 2 elements with pointers l & r) i.e, for i = 1 & i = 2, j is -1 in sorted array which is duplicate. it is skipped as it may lead to have 2 [-1,0,-1] if processed. Finally it avoids duplicate triplet startings.
                continue
            l, r = i + 1, len(nums) - 1
            while l < r: # O(n) per i
                three_sum = j + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([j, nums[l],  nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res

