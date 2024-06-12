class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_dict = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in index_dict:
                return [index_dict[complement], index]
                # return [index_dict.get(complement), index]
            index_dict[value] = index


solution = Solution()
result = solution.twoSum([2, 5, 7, 9], 9)
print(result)
