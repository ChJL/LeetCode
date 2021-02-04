# Tag: Linked List, Two Pointers
'''
Return true if there is a cycle in the linked list. Otherwise, return false.
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

SOL: official solution in Leetcode page:

using two pointers with different speed go through the linked list,
if the faster one arrive None -> loop do not exist
if the faster one and slower one meet each other -> loop exist

'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True