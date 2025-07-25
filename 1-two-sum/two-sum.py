class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(N^2) - less optimised.
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        
# We can use 2 pointer technique but it runs in O(N LOG N) time to first sort the array (as it is not) and would mess up with the original indices. but we can still do it if we want to like below:
        # time - O(n log n)
        # space - O(n)

        # indexed = [(j, i) for i, j in enumerate(nums)] # store index, value pairs.
        # indexed.sort() # now sort the indexed
        # l, r = 0, len(indexed) - 1
        # while l < r:
        #     curr_sum = indexed[l][0] + indexed[r][0]
        #     if curr_sum == target:
        #         return [indexed[l][1], indexed[r][1]]
        #     elif target > curr_sum:
        #         l += 1
        #     else:
        #         r -= 1
        # return [l, r]

# -----------------------------------------------------
        # time - O(N) - most optimised solution using HASHMAP
        # space - O(n)
        hashmap = defaultdict(int)
        for i,j in enumerate(nums):
            comp = target - j
            if comp in hashmap: # wont get key error since it checks if the key comp exists in the dictionary before accessing it with hashmap[comp]
                return [hashmap[comp],i]
            hashmap[j] = i


