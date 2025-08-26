# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # time - O(n log k) - where N = total nodes, k = number of lists
        # space - O(k) - for the heap
        # if not lists:
        #     return None
        # heap = []
        # for i, node in enumerate(lists):
        #     if node: # we dont want the null nodes
        #         heapq.heappush(heap, (node.val, i, node)) # then order by i if values are equal to compute (cant do this by node) & here, we only push the head node of each list into the heap.
        # dummy = ListNode() # creating dummy node to simplify list construction
        # curr = dummy # Pointer to build the result list
        # while heap:
        #     val, i, node = heapq.heappop(heap) # unpacking the tuple & pop smallest ele
        #     curr.next = node # Attach the node to the result list
        #     curr = node # moving the curr pointer forward to add upcoming ele from there
        #     if node.next:
        #         heapq.heappush(heap, (node.next.val, i, node.next)) # This keeps the heap updated with the current smallest node from each list. i.e., you push the next node from the same list (from which the node was popped)
        # return dummy.next

        # The heap will initially contain:
# [(1, 0, node0), (1, 1, node1'), (2, 2, node2)]
# Each time the smallest node is popped and the next node from the same list is pushed in. This continues until the heap is empty and all nodes are merged.

        # INTUITION - Very Similar to Merge two sorted lists.
        # time - O(n log k)
        # space - O(k) # merged_list stores up to k references total across all rounds and each item in merged_list is just a pointer, not a copy of actual linked list nodes.

        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1: # Merging two lists is easy with your merge() function. But if there are more than two, we need to do this repeatedly until everything is combined into a single list, so is this while loop
            merged_list = []
            for i in range(0, len(lists), 2): # we have to compare 2 nodes then next nodes.
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                merged_list.append(self.merge(l1, l2)) # recursively reduces the lists to 1
            lists = merged_list
        return lists[0] # now len(lists)==1 and we need the linkedlist (inner one) in list of linkedlists.

    def merge(self, l1, l2): # a helper fxn to merge the upcoming 2 lists
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
