class Solution:
    def longestPalindrome(self, s: str) -> int:
        # time - O(n) space - O(1)
        hash = defaultdict(int)
        flag = False
        counter = 0
        
        for i in s:
            hash[i] += 1
        for i in hash.values():
            if i % 2 == 0:
                counter += i
            elif i % 2 == 1:
                counter += i - 1
                flag = True
        
        return counter if not flag else counter + 1
