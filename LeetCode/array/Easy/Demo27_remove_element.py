class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k


# if __name__ == "__main__":
solution = Solution()

nums = [3, 2, 2, 3]
val = 3
length = solution.removeElement(nums, val)
print(nums[:length])  # 输出: [2, 2]

nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
length = solution.removeElement(nums, val)
print(nums[:length])  # 输出: [0, 1, 3, 0, 4]

