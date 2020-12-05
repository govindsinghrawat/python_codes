##########
#Question#
##########
'''
URL: https://leetcode.com/problems/reverse-linked-list/

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

'''


##########
#Solution#
##########
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head == None or head.next == None:
            return head
        
        nextNode = self.reverseList(head.next)
        head.next.next = head;
        head.next = None;
        return nextNode;
    
    def reverseList1(self, head: ListNode) -> ListNode:
        
        previousNode = None
        while head != None:
            nextNode = head.next
            head.next = previousNode
            previousNode = head
            head = nextNode
        
        return previousNode
        
    
        
        
