##########
#Question#
##########
'''
URL: https://leetcode.com/problems/path-sum/

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

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
    # runningTotal = 0
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return sum == -1
        else: 
            return_value = False 

            running_sum = sum - root.val  

            if(running_sum == 0 and root.left == None and root.right == None): 
                return True 

            if root.left is not None: 
                return_value = return_value or self.hasPathSum(root.left, running_sum) 
            if root.right is not None: 
                return_value = return_value or self.hasPathSum(root.right, running_sum) 

            return return_value  
    
    
