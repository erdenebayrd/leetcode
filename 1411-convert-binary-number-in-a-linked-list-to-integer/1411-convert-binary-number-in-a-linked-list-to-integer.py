# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        res = f"{head.val}"
        while head.next is not None:
            head = head.next
            res += f"{head.val}"
        return int(res, 2)