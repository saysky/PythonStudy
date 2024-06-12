class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # num_dict = {}
        # for i in range(len(nums)):
        #     if nums[i] in num_dict and i - num_dict[nums[i]] <= k:
        #         return True
        #     num_dict[nums[i]] = i
        # return False

        # [1,2,3,1,2,3], k=2
        num_set = set()
        for i, num in enumerate(nums):
            # if (i - k - 1) >= 0:
            if i > k:
                num_set.remove(nums[i - k - 1])
            if num in num_set:
                return True
            num_set.add(num)
        return False