class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # time - O(n)
        # space - O(1)
        # o = len(s)
        # for i in range(len(s)-1,-1,-1):
        #     s.append(s[i])
        # del s[:o:]

        # another best way is to take 2 pointers at 1st and last positions and keep swapping them until l < r.
        # time - O(n)
        # space - O(1)

        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

