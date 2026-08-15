# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = []
        q= deque([root])
        ltr = True

        while q:
            l_size = len(q)
            level = []

            for _ in range(l_size):
                node = q.popleft()
                level.append(node.val)  

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

            if not ltr:
                level.reverse()

            res.append(level)
            ltr = not ltr

        return res
        