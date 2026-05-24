# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # time: O(N ^ 2)
        # space: O(1)
        # method: simulation of insertion sort in singly linked list

        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = dummy.next

        while curr:
            nested_prev, nested_curr = dummy, dummy.next
            while nested_curr != curr and nested_curr.val < curr.val:
                nested_curr = nested_curr.next
                nested_prev = nested_prev.next
            
            if nested_curr == curr:
                curr = curr.next
                prev = prev.next
                continue

            # swap nodes
            prev.next = curr.next
            nested_prev.next = curr
            curr.next = nested_curr

            curr = prev.next
        return dummy.next