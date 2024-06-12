class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1 = 1   =》1
        # 2 = 11,2  =》2
        # 3 = 111,12,21 =》3
        # 4 = 1111,211,121,112,22  =》5
        # 5 = 11111,2111,1211,1121,1112,221,212,122  =》8
        if n == 1 or n == 2:
            return n
        nums = [0] * n
        nums[0], nums[1] = 1, 2
        for i in range(2, n):
            nums[i] = nums[i - 1] + nums[i - 2]
        return nums[-1]
