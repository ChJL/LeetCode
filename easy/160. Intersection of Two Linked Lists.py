# Tag: Linked List

'''
Write a program to find the node at which the intersection of two singly linked lists begins.

SOL:
official solution in leetcode pages:
Maintain two pointers pA and pB initialized at the head of A and B, respectively. Then let them both traverse through the lists, one node at a time.
When pA reaches the end of a list, then redirect it to the head of B (yes, B, that's right.); similarly when pB reaches the end of a list, redirect it the head of A.

If at any point pA meets pB, then pA/pB is the intersection node.

'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if (headA is None) or (headB is None):
            return None
        
        Apoint = headA
        Bpoint = headB
        
        while Apoint != Bpoint:
            Apoint = headB if Apoint is None else Apoint.next
            Bpoint = headA if Bpoint is None else Bpoint.next
        
        return Apoint