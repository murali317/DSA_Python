class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # INTUITION - we have to get common prefixes from all strings and also have to compare with shortest string only to avoid IndexError if we accidentally overflow.
        # time - O(n log n + m) - m is length of the shortest string (for char comparison).
        # space - O(n)

        if not strs:
            return ''
        l = ''
        arr = sorted(strs) # lexicographically - ["flight", "flow", "flower"]
        # for i in range(len(sorted(strs, key = len)[0])): - When you’re comparing characters across all strings to find a common prefix, the common prefix can’t be longer than the shortest string.
        for i in range(min(len(arr[0]), len(arr[-1]))): # as it's sorted, no need to check in between strings, only check first & last(most unlikely having similar chars of 1st).
            if arr[0][i] != arr[-1][i]:
                return l
            else:
                l+=arr[0][i]
        return l
            
