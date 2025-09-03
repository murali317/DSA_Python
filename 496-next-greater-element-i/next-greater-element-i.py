class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # INTUITION - 1st loop over nums2 and add to stack, also check if cur element > stack[-1] if yes -> pop and add to hashmap {popped: cur element} so that we'll have track of next greater element. If not -> add -1 to those elements in hashmap. Append from hashmap to res and return.
        
        # time - O(n+m) 
        # space - O(n+m) - O(n) for stack and hashing, O(m) for res

        stack, res = [], []
        hashing = {} # O(n) space where n = length of nums2
        for i in nums2: # O(n) time where n = len(nums2).
            while stack and i>stack[-1]:
                hashing[stack.pop()] = i # {1: 3, 3: 4}, we should pop that processed element to avoid processing it again to -1. its greater element is noted so should not keep it after that.
            stack.append(i)
        while stack: # [4, 2]
            hashing[stack.pop()] = -1 # {1: 3, 3: 4, 2: -1, 4: -1}
        for i in nums1: # O(m) time where m = len(nums1)
            res.append(hashing[i])
        return res
