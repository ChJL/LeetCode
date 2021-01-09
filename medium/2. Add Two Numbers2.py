# Tag : Recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# recursive method
class Solution:
    
    def FunctionUse(self, l1: ListNode, l2: ListNode, diff) -> ListNode:
        if not l1 and not l2:
            if diff ==1:
                return ListNode(1)
            else:
                return
        
        curr_val = 0
        curr_val += diff
        curr_val += 0 if not l1 else l1.val
        curr_val += 0 if not l2 else l2.val
        
        diff = 0
        if curr_val >=10:
            diff = 1
            curr_val -= 10
        
        
        if not l1:
            l2.val = curr_val
            l2.next = self.FunctionUse(l1,l2.next,diff)
            return l2
        if not l2:
            l1.val = curr_val
            l1.next = self.FunctionUse(l1.next,l2,diff)
            return l1
        
        l1.val = curr_val
        l1.next = self.FunctionUse(l1.next, l2.next, diff)
        return l1
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.FunctionUse(l1,l2,0)

    
        
        
        

