# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        res = cur
        rem = 0
        while l1 is not None or l2 is not None:
            x = rem
            if l1 is not None:
                x += l1.val
                l1 = l1.next
            if l2 is not None:
                x += l2.val
                l2 = l2.next
            rem = x // 10
            cur.val = x % 10
            if l1 is not None or l2 is not None:
                cur.next = ListNode()
                cur = cur.next
        if rem > 0:
            cur.next = ListNode()
            cur = cur.next
            cur.val = rem
        return res
            