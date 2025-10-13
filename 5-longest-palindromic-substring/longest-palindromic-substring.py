class Solution:
    def longestPalindrome(self, s: str) -> str:
        #INTUITION - Expand around center approach - check for both odd-length & even-length palindromes. While checking compare the length of those and return the longest one.
        # time - O(n^2) space - O(1) since constant space not additional data structures
        # Since we check O(n) centers, and each takes at most O(n) time, so O(n^2)

        # def exp_ar_cen(left, right): # Expands outward from left and right as long as the characters match for a palindrome. Returns the last valid palindrome slice when expansion stops.
        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         left -= 1
        #         right += 1
        #     return s[left + 1:right]
        # longest = ''
        # for i in range(len(s)):
        #     odd_pal = exp_ar_cen(i, i)
        #     even_pal = exp_ar_cen(i, i+1)
            
        #     if len(odd_pal) > len(longest):
        #         longest = odd_pal
        #     if len(even_pal) > len(longest):
        #         longest = even_pal
        # return longest

        # ANOTHER WAY - WITHOUT A HELPER FUNCTION ----------------------
        # time - O(n^2)
        # space - O(1) - 2 variables & 2 pointers
        res = ''
        res_len = 0
        for i in range(len(s)):
            # Odd-lenth palindrome
            l, r = i, i
            while l >=0 and r < len(s) and s[l] == s[r]: # O(n) in W.C if entire string is palindrome
                if r - l + 1 > res_len: # to check if current pal_string is longer than previous 
                    res = s[l:r + 1]
                    res_len = r - l + 1
                l -= 1 # expanding backward from center (cur element)
                r += 1 # expanding forward from center (cur element)
            
            # Even-length palindrome
            l, r = i, i+1 # have to check cur and next element equal or not.
            while l >= 0 and r < len(s) and s[l] == s[r]: # O(n) in W.C if entire string is palindrome
                if (r - l + 1) > res_len:
                    res = s[l:r + 1]
                    res_len = r - l + 1
                l -= 1
                r += 1
        return res

