##########
#Question#
##########
'''
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head ==None or head.next == None:
            return head
        
        temp=temp2=ListNode()
        temp=head
        temp2=temp.next
        
        while temp2.next != None:
            # print("temp-->", temp)
            # print("temp2--->", temp2)
            if temp2.val == head.val:
                temp2=temp2.next
                
            else:
                head.next=temp2
                head=head.next
                temp2=temp2.next
        
        if head.val != temp2.val:
            # head.next != temp2:
            head.next = temp2
        else:
            head.next = None
        
            
        return temp

    
class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        pastVal = -1
        while head:
            if head.next:
                while head.next.val == head.val:
                    head.next = head.next.next
                    if not head.next:
                        break
            head = head.next
        return dummy.next
