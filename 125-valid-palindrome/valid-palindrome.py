class Solution:
    def isPalindrome(self, s: str) -> bool:
        # time - O(n^2) space - O(n)
        # import string

        # st = ''
        # for i in s:
        #     if (i in string.ascii_letters) or (i in string.digits):
        #         st += i.lower() # O(n^2) time for creation of string for each iteration
        # if st == st[::-1]: # O(n) for reverse checking
        #     return True
        # return False
    
    # --------------------------------------------------------------------------
    # INTUITION - just keep skipping non alphanumerics both from left & right and compare the valid ones.
    # NOTE - an empty string is also considered palindrome in most definitions.
        # time - O(n) space - O(1)
        # These loops skip non-alphanumeric characters, but each character is processed only once. so O(n) 
        # Since left and right always move forward or backward, no character is visited more than once. so O(n)
        # This runs at most N/2 times since left and right move toward the center.
        # finally, O(n) + O(n) = O(2n) = O(n) time

        left = 0
        right = len(s) - 1
        while left < right:
            while left< right and not s[left].isalnum(): # O(n) W.C for skipping multiple invalid chars from left side (or at the start) to consider only alnums.
                left += 1
            while left < right and not s[right].isalnum(): # for right side (or from end)
                right -= 1
            if s[left].lower() != s[right].lower(): # O(n) comparing valid chars
                return False
            left += 1
            right -= 1
        return True

        # eg: "Madam, I'm Adam!" -> True
        # eg: "#@%$%^" -> True
