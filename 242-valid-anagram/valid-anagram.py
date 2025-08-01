class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time - O(n)
        # space - O(n)
        # return sorted(s) == sorted(t)

        # time - O(n)
        # space - O(n)
        # from collections import Counter
        # c = Counter(s)
        # d = Counter(t)
        # return c == d

        # INTUITION - add every char to a hashmap with their frequency. now iterate over t, keep cutting down the frequency of all chars. atlast, if any char's frequency is still > 0 then its an extra char. Return False.
        # time - O(n) space - O(n)

        from collections import defaultdict
        hashmap = defaultdict(int) # dont use hashmap = {} since it raises keyError
        # defaultdict(int) means the default value will be 0
        for i in s:
            hashmap[i] += 1
        for j in t:
            hashmap[j] -= 1
        for k in hashmap.values():
            if k!=0:
                return False
        return True

