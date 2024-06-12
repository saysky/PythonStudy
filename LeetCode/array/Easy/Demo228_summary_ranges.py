class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        # result = []
        # if len(nums) == 0:
        #     return result
        # last_start = nums[0]
        # prev = nums[0]
        # i = 1
        # while i < len(nums):
        #     curr = nums[i]
        #     if (prev + 1) != curr:
        #         result.append((str(last_start) + '->' + str(prev)) if prev != last_start else str(prev))
        #         last_start = curr
        #     prev = curr
        #     i += 1
        # result.append((str(last_start) + '->' + str(prev)) if prev != last_start else str(prev))
        # return result

        # 输入：nums = [0, 1, 2, 4, 5, 7]
        # 输出：["0->2", "4->5", "7"]
        def format(i, j):
            return str(i) if i == j else str(i) + '->' + str(j)

        result = []
        if len(nums) == 0:
            return result
        slow = 0
        for fast in range(len(nums) - 1):
            if nums[fast] + 1 != nums[fast + 1]:
                result.append(format(nums[slow], nums[fast]))
                slow = fast + 1
        result.append(format(nums[slow], nums[fast + 1]))
        return result


print(Solution().summaryRanges([0, 1, 2, 4, 5, 7]))
assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
