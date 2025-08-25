# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy = ListNode(0, head) # if head is not given, we can give line 10
        # slow, fast = dummy, dummy
        # # dummy.next = head 
        # for i in range(n+1): # maintaining the 'n' nodes gap btw the slow & fast pointer so that ..
        #     fast = fast.next # now slow is at dummy (before the head), fast is at n steps ahead from the head.
        # while fast: # .. when slow and fast gets moved to next nodes one at a time, when fast exceeds the last node, slow will be just behind the nth node (nth node from the back of the LL) then we'll remove its next node from the LL and return the head of the LL.
        #     slow = slow.next
        #     fast = fast.next
        # slow.next = slow.next.next # slow.next (nth node from the back) is skipped.
        # return dummy.next

        # time - O(n)
        # space - o(1)
        length = 0
        fast = head
        while fast:
            length += 1
            fast = fast.next
        if length == n:
            head = head.next
            return head
        diff = length - n
        fast = head
        for i in range(diff - 1):
            fast = fast.next
        fast.next = fast.next.next
        return head
        