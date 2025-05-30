# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # time - O(n log k) - where N = total nodes, k = number of lists
        # space - O(k) - for the heap
        if not lists:
            return None
        heap = []
        for i, node in enumerate(lists):
            if node: # we dont want the null nodes
                heapq.heappush(heap, (node.val, i, node)) # then order by i if values are equal to compute (cant do this by node)
        dummy = ListNode() # creating dummy node to simplify list construction
        curr = dummy # Pointer to build the result list
        while heap:
            val, i, node = heapq.heappop(heap) # unpacking the tuple & pop smallest ele
            curr.next = node # Attach the node to the result list
            curr = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next)) # This keeps the heap updated with the current smallest node from each list.
        return dummy.next

        # The heap will initially contain:
# [(1, 0, node1), (1, 1, node1'), (2, 2, node2)]
# Each time the smallest node is popped and the next node from the same list is pushed in. This continues until the heap is empty and all nodes are merged.