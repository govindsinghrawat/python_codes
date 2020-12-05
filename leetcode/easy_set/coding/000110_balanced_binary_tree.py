##########
#Question#
##########
'''
URL: https://leetcode.com/problems/balanced-binary-tree/

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

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
class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def height(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        
        lheight=self.height(root.left)
        rheight=self.height(root.right)
        
        return max(lheight, rheight)+1

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return isBalanced(root)[0]
        
def isBalanced(root: TreeNode) -> (bool, int):
    if not root:
        return (True, 0)
    is_balanced, left_h = isBalanced(root.left)
    if not is_balanced:
        return (False, 0)
    is_balanced, right_h = isBalanced(root.right)
    if not is_balanced or abs(left_h - right_h) > 1:
        return (False, 0)
    return (True, max(left_h, right_h)+1)
