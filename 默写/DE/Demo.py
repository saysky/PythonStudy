class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # target = 7, nums = [ 2,3,1,2,4,3]
        # target = 2, nums = [10,20,30,2]
        # target = 5, nums = [1,2,3,2, 5]
        # 11 [1,2,3,4,5]
        # 找到最短子数组，子数组之和 >= target
        sum = 0
        min_len = len(nums) + 1
        slow, fast = 0, 0
        while fast < len(nums):
            sum += nums[fast]

            while sum >= target:
                min_len = min(min_len, fast - slow + 1)
                sum -= nums[slow]
                slow += 1

            fast += 1

        return min_len if min_len != (len(nums) + 1) else 0


print(Solution().minSubArrayLen(5, [1, 2, 3, 2, 5]))
print(Solution().minSubArrayLen(9, [1, 2, 3, 4, 5]))
print(Solution().minSubArrayLen(9, [10]))
