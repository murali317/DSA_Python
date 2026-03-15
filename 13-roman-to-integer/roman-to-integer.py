class Solution:
    def romanToInt(self, s: str) -> int:
        # INTUITION - Iterate through 's', minus a value if it is < next value (C<M, L<C, ...) else add it.  
        # time - O(n)
        # space - O(1)

        # d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        # total = 0
        # for i in range(len(s) - 1):
        #     if d[s[i]] < d[s[i+1]]:
        #         total -= d[s[i]]
        #     else:
        #         total += d[s[i]]
        # return total + d[s[-1]] # don't skipping the final character's value 1994

        # time - O(n)
        # space - O(1)
        
        hash = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000}
        curr = 0
        i = 0
        while i < len(s):
            if i+1 < len(s) and hash[s[i]] < hash[s[i+1]]:
                curr += hash[s[i+1]] - hash[s[i]]
                i += 2
            else:
                curr += hash[s[i]]
                i += 1

        return curr
