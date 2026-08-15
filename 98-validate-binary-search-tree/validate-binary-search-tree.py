# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l1=[]
        def helper(root):
            if root==None:
                return
            helper(root.left)
            if root!=None:
                l1.append(root.val)
            helper(root.right)
        helper(root)
        for i in range(1, len(l1)):
            if l1[i] <= l1[i-1]:
                return False
        return True




        