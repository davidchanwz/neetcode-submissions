# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1
        cnt = k
        def inorder(node):
            nonlocal cnt, res
            if not node:
                return
            else:
                inorder(node.left)
                cnt -= 1
                if cnt == 0:
                    res = node.val
                    return res
                inorder(node.right)
        inorder(root)
        return res