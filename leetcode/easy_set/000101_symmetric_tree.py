##########
#Question#
##########
'''
URL: https://leetcode.com/problems/symmetric-tree/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.

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
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None or (root.left == None and root.right == None):
            return True
        
        rightSubtree = []
        leftSubtree = []
        self.traverseLeftTree(root.left, leftSubtree)
        self.traverseRightTree(root.right, rightSubtree)
        
        print(leftSubtree)
        print(rightSubtree)
        
        if leftSubtree == rightSubtree:
            
            return True
        
        return False
    
    def traverseLeftTree(self, node: TreeNode, childs: List[int]):
        if node == None:
            childs.append('null')
            return
        childs.append(node.val)
        self.traverseLeftTree(node.left, childs)
        self.traverseRightTree(node.right, childs)
    
    def traverseRightTree(self, node: TreeNode, childs: List[int]):
        if node == None:
            childs.append('null')
            return
        childs.append(node.val)

        self.traverseRightTree(node.right, childs)
        self.traverseLeftTree(node.left, childs)
    
        
        
        

class Solution2:
    def isReflection(self, node1: TreeNode, node2: TreeNode):
        if (node1 == None and node2 == None): return True
        elif (node1 == None and node2 != None or node1 != None and node2 == None):
            return False
        elif (node1.val != node2.val):
            return False
        return self.isReflection(node1.left, node2.right) and self.isReflection(node1.right, node2.left)
    
    def isSymmetric(self, root: TreeNode) -> bool:
        if (root == None): return True
        return self.isReflection(root.left, root.right)
