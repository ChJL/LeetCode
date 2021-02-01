'''
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

SOL: iterative: use a tmp node to store the current, and then contact to the previous one

recursive:

class Solution:
# @param {ListNode} head
# @return {ListNode}
def reverseList(self, head):
    return self._reverse(head)

def _reverse(self, node, prev=None):
    if not node:
        return prev
    n = node.next
    node.next = prev
    return self._reverse(n, node)
'''

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
            
        return prev
            