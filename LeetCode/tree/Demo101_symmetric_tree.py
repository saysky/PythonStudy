# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 二叉树是否对称
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isSymmetricTree(p, q):
            if not p and not q:
                return True
            if (p and not q) or (not p and q):
                return False
            if p.val != q.val:
                return False
            return isSymmetricTree(p.left, q.right) and isSymmetricTree(p.right, q.left)

        if not root:
            return True
        return isSymmetricTree(root.left, root.right)