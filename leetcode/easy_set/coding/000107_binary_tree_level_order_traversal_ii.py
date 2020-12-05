##########
#Question#
##########
'''
URL: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        depth = self.maxDepth(root)
        final_list = []
        
        for h in range(1,depth+1):
            temp=[]
            self.getLevelNodes(root, h, temp)
            final_list.append(temp)
        
        return final_list[::-1]
            
    def getLevelNodes(self, root: TreeNode, level: int, temp: List[int]):
        if root==None:
            return
        if level == 1:
            temp.append(root.val)
        elif level > 1:
            self.getLevelNodes(root.left, level-1, temp)
            self.getLevelNodes(root.right, level-1, temp)
        
        
            
    
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
            
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1
