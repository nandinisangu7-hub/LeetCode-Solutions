# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return [] 
        d=deque([root])
        ans=[]
        while(d):
            size=len(d)
            l1=[]
            for i in range(size):
                node=d.popleft()
                l1.append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            ans.append(l1)
        return ans
        