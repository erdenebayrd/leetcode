# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedHead = ListNode()
        currentHead = reversedHead
        def reverseLinkedList(currentNode: Optional[ListNode]) -> None:
            nonlocal currentHead
            if currentNode is None:
                return
            reverseLinkedList(currentNode.next)
            currentHead.next = ListNode(currentNode.val)
            currentHead = currentHead.next
        reverseLinkedList(head)
        # print(reversedHead)
        # print(currentHead)
        return reversedHead.next