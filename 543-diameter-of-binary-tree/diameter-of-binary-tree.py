# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root==None:
                return 0
            left=helper(root.left)
            right=helper(root.right)
            l1[0]=max(l1[0],left+right)
            return 1+max(left,right)
        l1=[float('-inf')]
        helper(root)
        return l1[0]

        

        