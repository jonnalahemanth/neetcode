# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        pre_idx = [0]

        for i, val in enumerate(inorder):
            inorder_map[val] = i

        def dfs(start, end):
            if start>end:
                return None

            root_val = preorder[pre_idx[0]]
            pre_idx[0] += 1

            root = TreeNode(root_val)
            mid = inorder_map[root_val]
            root.left = dfs(start, mid-1)
            root.right = dfs(mid+1, end)

            return root

        return dfs(0, len(inorder)-1)



        