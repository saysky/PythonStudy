class Solution:
    '''
    https://leetcode.cn/leetbook/read/array-and-string/yf47s/
    找左右两侧之和相等的下标
    输入：nums = [1, 7, 3, 6, 5, 6]
    输出：3
    '''

    def pivotIndex(self, nums: list[int]) -> int:
        # for i in range(len(nums)):
        #     left = sum(nums[:i])
        #     right = sum(nums[i+1:])
        #     if left == right:
        #         return i
        # return -1
        total_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_num = total_sum - left_sum - nums[i]
            if right_num == left_sum:
                return i
            left_sum += nums[i]
        return -1


s = Solution()
assert s.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
assert s.pivotIndex([1, 2, 3]) == -1
assert s.pivotIndex([2, 1, -1]) == 0
