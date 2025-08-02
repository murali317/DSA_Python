class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # INTUITION - Take a hashmap and store the chars in s as you loop over. Also while checking chars from s, dont forget to check if chars in t were already processed or not (bijective/ one-to-one and onto).
        # time - O(n)
        # space - O(n)

        from collections import defaultdict
        h1 = defaultdict(str) # O(n) space if every char is unique in W.C
        st = set()
        for i in range(len(s)): # 1 loop is enough as both s and t are of same lengths.
            if s[i] in h1 and h1[s[i]] == t[i]:
                    continue # or pass
            elif s[i] not in h1: # st bcoz we also need to check if t[i] was already paired before or not. If yes, its a bad husband/wife \U0001f61c.
                if t[i] in st:
                    return False
                st.add(t[i])
                h1[s[i]] = t[i]
            elif s[i] in h1 and h1[s[i]] != t[i]:
                return False
        return True
