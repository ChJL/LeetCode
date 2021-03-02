# Tag: Linked List
'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. 
Return the linked list sorted as well.

Example1:
Input: head = [1,1,2]
Output: [1,2]

Example2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

SOL: if duplicate, simply move the link to the next one who's different.
'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        while head:
            if head.next is not None and head.val == head.next.val:
                if head.next.next is None:
                    head.next = None
                else:
                    head.next = head.next.next
            else:
                head = head.next
        
        return dummy.next