class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # time - O(n) space - O(n) uses extra space for hashmap
        # from collections import defaultdict
        # hashmap = defaultdict(int)
        # for i,j in enumerate(numbers):
        #     comp = target - j
        #     if comp in hashmap:
        #         return [hashmap[comp]+1, i+1]
        #     hashmap[j] = i


        l, r = 0, len(numbers) - 1
        while l<r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
        

        # using 2 pointers (like binary search but not, as we are not diving in half just traversing) is better as the input array is sorted.
        # time - O(n) space - O(1)
        # left, right = 0, len(numbers)-1
        # while left < right:
        #     s = numbers[left] + numbers[right]
        #     if s == target:
        #         return [left + 1, right + 1] #space - O(1) since its fixed
        #     elif s < target:
        #         left += 1
        #     else:
        #         right -= 1
        # return [left + 1, right + 1]
