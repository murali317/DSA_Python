# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # time - O(log n) space - O(1)
        l, r = 1, n # dont give l = 0 it could fail a test case as version 0 is not valid in the system
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid) == True:
                r = mid - 1
            else:
                l = mid + 1
        return l