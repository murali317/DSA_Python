class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # time - O(n)
        # space - O(k) not O(n) because set is storing at most k unique elements, not n
        # if the size grows till the length of array, the might be O(n) which is not the case in this problem.
        # l,s_sum,max_sum = 0,0,float(-inf)
        # s = set()
        # for r in range(len(nums)):
        #     while nums[r] in s:
        #         s.remove(nums[l])
        #         s_sum -= nums[l]
        #         l += 1
        #     s.add(nums[r])
        #     s_sum += nums[r]
        #     if r-l+1 == k:
        #         max_sum = max(max_sum, s_sum)
        #         s.remove(nums[l])
        #         s_sum -= nums[l]
        #         l += 1
        # return max_sum if max_sum != float(-inf) else 0

        l, s_sum, m_sum, s = 0, 0, float(-inf), set()
        for i in range(len(nums)):
            while nums[i] in s:
                s.remove(nums[l])
                s_sum -= nums[l]
                l += 1
            s.add(nums[i])
            s_sum += nums[i]
            if i-l+1 == k:
                m_sum = max(s_sum, m_sum)
                s_sum -= nums[l]
                s.remove(nums[l])
                l += 1
        return m_sum if m_sum != float(-inf) else 0

        
        