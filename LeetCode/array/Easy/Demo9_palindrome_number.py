class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # if x < 0 or (x % 10 == 0 and x != 0):
        #     return False
        # temp = x
        # reversed_x = 0
        # while temp > 0:
        #     reversed_x = reversed_x * 10 + (temp % 10)
        #     temp = temp // 10  # 整除
        # return reversed_x == x

        return str(x) == str(x)[::-1]
