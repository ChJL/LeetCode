# Tag: Recursion
# iterative method
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

EX:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

EX2:
Input: l1 = [0], l2 = [0]
Output: [0]

EX3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

'''

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        diff = 0
        while l1 or l2:
            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
                l2 = l2.next
            else: 
                l2_val = 0
                
            sum_val = l1_val + l2_val + tail.val

            mod = sum_val % 10
            
            if sum_val >= 10:
                diff = 1
            else :
                diff = 0
            
            tail.val = mod
            
            
            if l1 or l2 or diff:
                tail.next = ListNode(diff)
                tail = tail.next

        
        return dummy