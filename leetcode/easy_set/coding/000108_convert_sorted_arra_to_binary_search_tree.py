##########
#Question#
##########
'''
URL: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

'''


##########
#Solution#
##########

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        tree = self.createBST(nums, 0, len(nums)-1)
        return tree
    
    
    
    def createBST(self, nums: List[int], start:int, end:int) -> TreeNode:
        if start > end:
            return
        
        mid = start + (end - start) // 2
        node = TreeNode(nums[mid])
        node.left = self.createBST(nums, start, mid-1)
        node.right = self.createBST(nums, mid+1, end)
        
        return node
        
        
