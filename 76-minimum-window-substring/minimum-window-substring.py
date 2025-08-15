class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # INTUITION - Use a sliding window to find the smallest substring in s that contains all characters of t. Expand to include, shrink to optimize. 
# 1️⃣ Use a hashmap to count chars in t (what and how many you need).
# 2️⃣ Expand right to collect needed chars, decrease their counts, and track how many are still missing.
# 3️⃣ When all are found, move left to shrink the window while keeping it valid, and update the smallest result.

        # time - O(m+n)
        # space - O(n) - hashmap to store chars of 't' of length 'n' 
        
        hashmap = defaultdict(int)
        if not s or not t:
            return '' # if s or t is an empty string
        for i in t: # O(n)
            hashmap[i] += 1 # to store each character of t in a hashmap
        left = 0 # left end of the window
        min_len = float('inf')
        min_start = 0 # Start index of the minimum window
        c = len(t) # no of chars we still need to match
        for r in range(len(s)): # O(m)
            if s[r] in hashmap:
                if hashmap[s[r]] > 0:
                    c -= 1
                hashmap[s[r]] -= 1
            while c == 0:
                window_len = r - left + 1
                if window_len < min_len:
                    min_len = window_len # 6 
                    min_start = left
                if s[left] in hashmap: # the exact first 'if' part is repeated here.
                    hashmap[s[left]] += 1 # increment back, cause we r going to move forward leaving this.
                    if hashmap[s[left]] > 0: # as we removed 'A' we again need it.
                        c += 1 # until then, the window is no longer valid.
                left += 1 # shrink the window from left side.
        return s[min_start:min_start+min_len] if min_len != float('inf') else ''