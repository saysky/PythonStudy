class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # num_set = set()
        # for num in nums:
        #     if num in num_set:
        #         return True
        #     num_set.add(num)
        # return False

        return len(nums) != len(set(nums))
