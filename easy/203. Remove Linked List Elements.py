# Tag: Linked List
'''
Remove all elements from a linked list of integers that have value val.
Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

SOL: iteratively compare the value,--> could be improved
'''
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        tail = dummy
        while head:
            if head.val != val:
                tail.next = ListNode(head.val)
                tail = tail.next
            head = head.next
        return dummy.next