# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        vals = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            vals.append(node.val)
            dfs(node.right)

        dfs(root)

        dummy = TreeNode(0)
        curr = dummy

        for v in vals:
            curr.right = TreeNode(v)
            curr = curr.right

        return dummy.right