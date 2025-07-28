class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # INTUITION - take a map of {0 -> 1}. Iterate over the nums and sum the elements. at each step, if (sum - k) in map, increment count to frequency of that diff in map. if not present, add that to map as below.

        # time - O(n)
        # space - O(n)
        total = 0 # prefix sum or running sum
        count = 0 # to track no of subarrays we find
        hash = {0:1} # dictionary to map prefix_sum → frequency to handle the case when a prefix sum itself equals k. and we start with 0 allowing us to handle subarrays that begin from index 0.
        for i in nums:
            total += i
            if total - k in hash:
                count += hash[total - k]
            hash[total] = hash.get(total, 0) + 1
        return count
            