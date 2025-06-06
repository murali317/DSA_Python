class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # time - O(n + k) space - O(k)
        # d={}
        # l=[]
        # for i in nums:
        #     if i not in d:
        #         d[i]=1
        #     else:
        #         d[i]+=1 # O(k) t & s as k elements would be in d not complete n.
        # for i,j in d.items():
        #     l.append(j) # O(k) time & space
        # for i,j in d.items():
        #     if j==max(l):
        #         return i

        # time - O(n log n) space - O(n) worst case, O(1) average case for in-place sorting
        # nums.sort()
        # return nums[len(nums)//2] # O(1) space for indexing

        # BOYER - MOORE ALGORITHM ☠️\U0001f635
        # time - O(n) space - O(1) 
        res, count = 0, 0
        for i in nums:
            if count == 0:
                res = i
            count += (1 if i == res else -1)
        return res