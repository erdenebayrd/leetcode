# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        previousNode = None
        tail = head
        for _ in range(left - 1):
            previousNode = tail
            tail = tail.next
        
        currentHead = tail
        previousNodeReversed = None
        for _ in range(right - left + 1):
            nextNode = currentHead.next
            currentHead.next = previousNodeReversed
            previousNodeReversed = currentHead
            currentHead = nextNode
        
        # print(previousNodeReversed)
        tail.next = currentHead
        # print(previousNodeReversed)
        if not previousNode:
            return previousNodeReversed
        previousNode.next = previousNodeReversed
        # print(previousNode)
        return head