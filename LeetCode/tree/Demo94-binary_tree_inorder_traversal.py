# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归中序遍历二叉树
class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        def inorder(root, result):
            if not root:
                return None
            inorder(root.left, result)
            result.append(root.val)
            inorder(root.right, result)

        result = []
        inorder(root, result)
        return result
