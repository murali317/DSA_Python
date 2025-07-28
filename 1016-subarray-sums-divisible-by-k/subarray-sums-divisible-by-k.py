class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # INTUITION - same as subarray sum equals K, instead of adding sum to hash, add mod (%) as keys and its frequency as values.
        # time - O(n)
        # space - O(k)
        total = 0
        count = 0
        hash = {0:1}
        for i in nums:
            total += i
            m = (total % k + k) % k # to hanlde -ve numbers
            if m in hash:
                count += hash.get(m, 0) # similar to hash[m] += 1 but its a safe lookup.
            hash[m] = hash.get(m, 0) + 1
        return count