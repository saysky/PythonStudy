class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [0 1 2 4]
        [1 2 0 4]
        """
        k = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[k] = num
                k += 1
        nums[k:] = [0] * (len(nums) - k)
