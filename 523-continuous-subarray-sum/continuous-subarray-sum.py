class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # INTUITION - When two prefix sums have the same remainder modulo k, the difference between them is divisible by k.
        # ✅ So Why Store mod values?
# We store all mod values of the prefix sum (not just 0) because:
# If prefix_sum % k == r at index i, and we later see the same r at index j,
# Then the sum of the subarray from index i+1 to j is divisible by k.
        # time - O(n)
        # space - O(min(n,k))

        remainder = {0 : -1} # handles subarrays starting at index 0 
        total = 0
        for i, n in enumerate(nums): # we need indices as well.
            total += n
            r = total % k
            if r not in remainder: # if mod value not seen, store its index
                remainder[r] = i
            elif i - remainder[r] > 1: # if distance btw current index and stored index is atleast 2 i.e., in 1st eg: 2 - 0 = 2 which is > 1
                return True
        return False
