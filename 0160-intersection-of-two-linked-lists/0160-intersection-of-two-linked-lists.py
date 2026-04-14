# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # time: O(N + M)
        # space: O(1)
        # method: LCA of a tree
        
        def getLength(currentHead: ListNode) -> int: # O(N)
            length = 0
            while currentHead:
                currentHead = currentHead.next
                length += 1
            return length
        
        lengthA = getLength(headA)
        lengthB = getLength(headB)
        diff = abs(lengthA - lengthB)
        if lengthA > lengthB:
            while diff:
                diff -= 1
                headA = headA.next
        else:
            while diff:
                diff -= 1
                headB = headB.next
        
        result = None
        while headA and headB:
            if headA == headB:
                result = headA
                break
            headA = headA.next
            headB = headB.next
        return result