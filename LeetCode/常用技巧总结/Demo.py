def get_prefix_sum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums

print(get_prefix_sum([1,2,3,4]))