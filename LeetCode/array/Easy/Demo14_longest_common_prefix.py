class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # if len(strs) == 1:
        #     return strs[0]
        # lens = [len(s) for s in strs]
        # min_len = min(lens)
        # temp = strs[lens.index(min_len)]
        #
        # for i in range(len(temp)):
        #     for s in strs:
        #         if s[i] != temp[i] :
        #             return temp[0:i]
        # return temp

        min_str = min(strs, key=len)
        for i in range(len(min_str)):
            for s in strs:
                if s[i] != min_str[i]:
                    return min_str[0:i]
        return min_str


solution = Solution()
result = solution.longestCommonPrefix(["flower222222", "flow", "floight"])
# result = solution.longestCommonPrefix(["abca","aba","aaab"])
print(result)
