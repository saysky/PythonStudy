# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        # 1 2 3 4 5
        # 1 2 3 4 5 6
        def create_tree(low, high):
            if low > high:
                return None
            mid = (low + high) // 2
            root_node = TreeNode(nums[mid])
            root_node.left = create_tree(low, mid - 1)
            root_node.right = create_tree(mid + 1, high)
            return root_node

        return create_tree(0, len(nums) - 1)

s = Solution()
root = s.sortedArrayToBST([-10,-3,0,5,9])
print(root)