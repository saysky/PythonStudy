class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # nums.sort()
        # # [1,1,2]
        # # [1, 2,2,2]
        # # [1,2,2,2, 3]
        # # [1, 2, 2,2, 3, 3]
        # return nums[len(nums) // 2]

        # candidate = 0
        # count = 1
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[candidate]:
        #         count += 1
        #     else:
        #         count -= 1
        #     if count <= 0:
        #         candidate = i
        #         count = 1
        # return nums[candidate]

        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            # count = count + 1 if num == candidate else  count - 1
            count += 1 if num == candidate else -1
        return candidate
