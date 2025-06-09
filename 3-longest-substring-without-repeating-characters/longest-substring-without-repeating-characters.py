class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we will take 2 pointers to check if substring exists without any duplicates and move the sliding window(nothing but those 2 pointers) dynamically .
        # time - O(n) bcoz of O(n) loops and both 2 pointers traverse 's' atmost once
        # space - O(1) since st stores at most 26 lowercase English letters.
        st = set()
        left = 0 # left pointer of the sliding window
        max_len = 0
        for right in range(len(s)):
            while s[right] in st: # move left pointeruntil that duplicate is still in the set. Because a character might be repeated multiple time and while continuosuly removes them. # if condition fails for s = 'abba' 
                st.remove(s[left])
                left += 1
            st.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len