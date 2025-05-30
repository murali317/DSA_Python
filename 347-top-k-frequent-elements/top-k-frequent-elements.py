class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # INTUITION - for this kind of problem, we have to group the elements with their count (using hashmap) to sort them in descending order, so that the answer becomes first k elements. Here you don't need the full sorted array. You just need Top K elements. So it's wasteful to fully sort everything. ❌ So first go with hashmap + sorting then turn to heap for optimized code.

        # time - O(n log n) space - O(n)
        # from collections import defaultdict
        # l = []
        # hashmap = defaultdict(int)
        # for i in nums:
        #     hashmap[i] += 1
        # for i in hashmap:
        #     l.append((i, hashmap[i]))
        # l_sorted = sorted(l, key = lambda x: x[1], reverse = True) # time - O(n log n)
        # return [i[0] for i in l_sorted[:k]]

        # -------------- HEAP --------------------
        # time - O(n + m log k) d: is built from nums and will have at most m keys, where m ≤ n
        # space - O(m + n) in W.C m=n if all elements in nums are unique

        import heapq
        d = defaultdict(int)
        min_heap = [] # using a min_heap of size k
        for i in nums: d[i] += 1 # counting the freqs
        for ele, freq in d.items(): 
            heapq.heappush(min_heap, (freq, ele)) # heap by freq
            if len(min_heap) > k: # should not exceed size k(so remove least frequent elements)
                heapq.heappop(min_heap) # remove least frequent
        return [ele for freq, ele in min_heap] # since its a list of tuples [(freq, ele)]
        
