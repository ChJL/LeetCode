# Tag: Linked List, Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# iteratively
'''
def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        count = 1
        tmp = None
        dummy= ListNode()
        dummy.next = head
        while head:
            if count%2 and head.next:
                tmp = head.val
                head.val = head.next.val
            if not count%2:
                head.val = tmp
            
            head = head.next
            count +=1
        
        return dummy.next
'''
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # recursively, draw a graph to better understand it.
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs(tmp.next)
            tmp.next = head
            return tmp
        return head