# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s=0
        d=deque([root])
        while(d):
            node=d.pop()
            if node.val>=low and node.val<=high:
                s=s+node.val
            if node.left:
                d.append(node.left)
            if node.right:
                d.append(node.right)
        return s




        