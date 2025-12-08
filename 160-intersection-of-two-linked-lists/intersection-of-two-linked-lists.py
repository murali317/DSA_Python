# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # time - O(m + n) (Finding length + aligning + traversing) - O(n1​)+O(n2​)+O(max(n1​,n2​))+O(min(n1​,n2​))
        # space - O(1) no extra space needed
        a = headA
        b = headB
        l1 = 1
        l2 = 1
        while a.next is not None: # O(n)
            l1 += 1
            a = a.next
        while b.next is not None: # O(m)
            l2 += 1
            b = b.next
        if l1>l2: # O(max(n, m))
            for i in range(l1-l2): # headA forward by (l1 - l2) nodes.
                headA = headA.next
        else:
            for i in range(l2-l1): # headB forward by (l2 - l1) nodes.
                headB = headB.next
        while headA and headB: # O(min(n, m))
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None