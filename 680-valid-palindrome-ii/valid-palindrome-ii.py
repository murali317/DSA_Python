class Solution:
    def validPalindrome(self, s: str) -> bool:
        # INTUITION - if one mismatch is found, its ok, keep checking. but if more than 1 is found, not a palindrome. Otherwise Palindrome.
        # time - O(n)
        # space - O(1) # no recursion stack or no extra memory.

        def isPalindrome(x, y):
            while x<y: 
                if s[x] != s[y]:
                    return False
                x += 1
                y -= 1
            return True
        
        l, r = 0, len(s) - 1
        while l<r: # cause if l>=r we are done checking.
            if s[l] != s[r]: # one mismatch is found, now we have to check if there's a second mismatch or not. if yes, boom not a pal, otherwise check again through helper function.
                return isPalindrome(l+1, r) or isPalindrome(l, r-1) # O(n) we only scan at most 2n characters in total which involves 1 full scan.
            l += 1
            r -= 1
        return True