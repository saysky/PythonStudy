# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 判断2个树是否相同
class Solution(object):
    # def isSameTree(self, p, q):
    # def isSame(p, q):
    #     if not p and not q:
    #         return True
    #     if (not p and q) or (p and not q):
    #         return False
    #     if p.val != q.val:
    #         return False
    #     lresult = isSame(p.left, q.left)
    #     rresult = isSame(p.right, q.right)
    #     return lresult and rresult
    #
    # return isSame(p, q)

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
