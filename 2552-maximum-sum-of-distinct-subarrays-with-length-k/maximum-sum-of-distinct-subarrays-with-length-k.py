class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # time - O(n)
        # space - O(k) not O(n) because set is storing at most k unique elements, not all n
        # if the size grows till the length of array, the might be O(n) which is not the case in this problem.
        # l,s_sum,max_sum = 0,0,float(-inf)
        # s = set()
        # for r in range(len(nums)):
        #     while nums[r] in s: # have to remove until that duplicate is present and not O(n^2) since it just moves foward and doesn't reprocess old elements. - amortized
        #         s.remove(nums[l]) # O(1)
        #         s_sum -= nums[l]
        #         l += 1
        #     s.add(nums[r]) # O(1)
        #     s_sum += nums[r]
        #     if r-l+1 == k:
        #         max_sum = max(max_sum, s_sum)
        #         s.remove(nums[l])
        #         s_sum -= nums[l]
        #         l += 1
        # return max_sum if max_sum != float(-inf) else 0

        # time - O(n)
        # space - O(k)
        start = 0; res = float(-inf); total = 0; d = defaultdict(int)
        for end in range(len(nums)):
            total += nums[end]
            d[nums[end]] += 1
            while d[nums[end]] > 1: # use while instead of 'if' to filter duplicates until it becomes duplicates-free.
                total -= nums[start]
                d[nums[start]] -= 1
                start += 1
            if (end - start + 1) == k:
                res = max(res, total)
                total -= nums[start]
                d[nums[start]] -= 1
                start += 1
            
        return res if res != float(-inf) else 0

        
        