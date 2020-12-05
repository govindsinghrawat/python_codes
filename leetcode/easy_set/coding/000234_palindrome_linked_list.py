##########
#Question#
##########
'''
URL: https://leetcode.com/problems/palindrome-linked-list/

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

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
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        temp=head
        oldList = []
        
        while temp:
            oldList.append(temp.val)
            temp=temp.next
            
        n=len(oldList)
        # print(n, oldList)
        for i in range(n//2):
            if oldList[i] !=oldList[n-i-1]:
                return False
            
        return True
