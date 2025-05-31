class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # INTUITION - First turn this list to a max-heap by negating the values, pop 1st & 2nd largest of them, subtract and push it to the heap until only 1 element is left. In btw, if both 1st&2nd largest are equal, continue (dont bother as they will be popped and not pushed).
        # time - O(n log n) # O(n) + O(n) + O(n log n)
        # space - O(n)
        import heapq
        if not stones:
            return None
        heap = [-x for x in stones] # negate the values [-2,-7,-4,-1,-8,-1] # O(n)
        heapq.heapify(heap) # convert list to a heap
        while len(heap) > 1: # O(n)
            first = -heapq.heappop(heap) # largest # O(log n)
            second = -heapq.heappop(heap) # second-largest # O(log n)
            if first != second:
                heapq.heappush(heap, -(first-second)) # we have to push negate values  to heap otherwise smallest values would start coming out.
        return -heap[0] if heap else 0

            