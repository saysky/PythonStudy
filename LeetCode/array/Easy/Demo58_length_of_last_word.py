class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if len(s) == 0:
        #     return 0
        # arr = s.split()
        # return len(arr[-1])
        arr = s.split()
        return len(arr[-1]) if arr else 0
