class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums.sort()
        # 1 2 2
        # 1 1 2 3 3
        # 2 2 3
        i = 0
        # while i < (len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         i += 2
        #     else:
        #         return nums[i]
        # return nums[-1]
        result = 0
        for num in nums:
            result = result ^ num  # 异或
        return result
