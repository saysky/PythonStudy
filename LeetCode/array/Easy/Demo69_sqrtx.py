class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 3 4 9 10
        k = 1
        while k * k <= x:
            k += 1
        return k - 1
