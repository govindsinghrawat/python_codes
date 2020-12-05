##########
#Question#
##########
'''
URL: https://leetcode.com/problems/minimum-depth-of-binary-tree/
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000

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
    def minDepth(self, root: TreeNode) -> int:
        return self.height(root)
            
        
    def height(self, node: TreeNode) -> int:
        if node == None:
            return 0
        
        if node.left == None and node.right == None:
            return 1
        
        if node.left == None:
            return self.height(node.right)+1
        
        if node.right == None:
            return self.height(node.left)+1
        
        return min(self.height(node.right), self.height(node.left) )+1
        
