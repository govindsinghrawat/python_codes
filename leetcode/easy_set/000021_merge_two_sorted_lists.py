##########
#Question#
##########
'''
URL: https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

 

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.

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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = ListNode()
        a=l1
        b = ListNode()
        b=l2
        c = ListNode()
        d = c
        
        if not l2:
            return l1
        
        if not l1:
            return l2
        
    
        while a != None and b !=None:
            if a.val <= b.val:
                d.val=a.val
                a = a.next
            else:
                d.val=b.val
                b=b.next
            d.next = ListNode()
            d=d.next
                
        while a!=None:
            d.val = a.val
            d.next = ListNode()
            d=d.next
            a=a.next
        
        while b!=None:
            d.val = b.val
            d.next = ListNode()
            d=d.next
            b=b.next
        

        d=c
        while (d.next).next !=None:
            print(d.val)
            d=d.next
        
        d.next=None
        
        return c



###########
#Solution2#
###########
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=temp=ListNode()
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        
        while(l1 and l2):
            if(l1.val<l2.val):
                temp.next=l1
                temp=temp.next
                l1=l1.next
            else:
                temp.next=l2
                temp=temp.next
                l2=l2.next
            if(l2):
                temp.next=l2
            if(l1):
                temp.next=l1
        return head.next
