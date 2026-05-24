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

        dummy = ListNode(float('-inf'), head)
        prev = dummy
        curr = dummy.next

        while curr:
            if prev.val <= curr.val: # already in sorted order
                prev, curr = curr, curr.next
                continue
            
            node = dummy
            while node.next.val <= curr.val:
                node = node.next
            
            # swapping
            prev.next = curr.next
            curr.next = node.next
            node.next = curr

            curr = prev.next
        
        return dummy.next