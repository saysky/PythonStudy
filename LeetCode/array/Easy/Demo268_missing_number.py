class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        set_nums = set(nums)
        for i in range(len(nums)):
            if i not in set_nums:
                return i
        return len(nums)


s = Solution()
assert s.missingNumber([3, 0, 1]) == 21, "错了"
