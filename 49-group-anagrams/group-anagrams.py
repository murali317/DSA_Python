class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        # INTUITION - group the strs as key is sorted value(s) and its value is normal elements (before sorting). Then return the values.
        # time - O(n.k log k)
        # space - O(n.k)

        hash = defaultdict(list)
        arr = []
        for i in strs: # O(n)
            j = ''.join(sorted(i)) # O(k log k) time k is length of each word, O(n.k) space
            # if j in hash: # this part is not required as it is defaultdict(list), by default 0 only.
            #     hash[j].append(i)
            # else:
            #     hash[j] = [i]
            hash[j].append(i)

        # for i in hash.values():
        #     arr.append(i)
        # return arr
        return list(hash.values()) # O(n) time for flattening, 