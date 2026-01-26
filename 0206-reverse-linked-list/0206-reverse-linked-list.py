# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ----------- iterative approach -----------
        # previousNode = None
        # currentNode = head
        # while currentNode:
        #     nextNode = currentNode.next
        #     currentNode.next = previousNode
        #     previousNode = currentNode
        #     currentNode = nextNode
        # return previousNode

        # ----------- recursive approach -----------
        reversedHead = ListNode()
        currentHead = reversedHead
        def reversedLinkedList(currentNode: Optional[ListNode]) -> None:
            nonlocal currentHead
            if currentNode is None:
                return
            reversedLinkedList(currentNode.next)
            currentHead.next = ListNode(currentNode.val)
            currentHead = currentHead.next
        reversedLinkedList(head)
        return reversedHead.next