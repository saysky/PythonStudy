class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # for i in range(len(haystack) - len(needle) + 1):
        #     flag = True
        #     j = 0
        #     while flag and j < len(needle):
        #         if haystack[i+j] != needle[j]:
        #             flag = False
        #         j += 1
        #     if flag:
        #         return i
        # return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:].startswith(needle):
                return i
        return -1
