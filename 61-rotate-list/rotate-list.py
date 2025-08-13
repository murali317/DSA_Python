# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # time - O(k * n) time limit exceeded (inefficient) for large k
        # O(k * n) - because we are iterating n times for each of k rotations
        # space - O(1)

        # if not head or not head.next or k == 0:
        #     return head
        # for i in range(k):
        #     slow = head
        #     fast = head.next
        #     while fast and fast.next: # to prevent error for LL having less than 2 nodes
        #         slow = slow.next
        #         fast = fast.next
        #     fast.next = head # connect last node to head
        #     slow.next = None # break the link
        #     head = fast # updating new head after each iteration
        # return head
        
        # IINTUITION - for these kind of problems with k < length of LL and > length of LL, we have to normalize with its length (k = k % length). cause if k = 4 -> length - k - 1 = 3-4-1 = -2. for loop wont run with (-2)
        # time - O(n) # all loops are of O(n)
        # space - O(1) LL is modified in-place and no extra ds(arrays, hashs) are used
        if not head or not head.next or k == 0:
            return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        k = k % length # normalize 'k' to avoid extra rotations time - O(1)
        if k == 0:
            return head
        slow = head
        for i in range(length - k - 1):
            slow = slow.next
        new_head = slow.next
        slow.next = None
        tail.next = head
        return new_head

         