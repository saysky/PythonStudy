class Solution:
    # https://leetcode.cn/leetbook/read/array-and-string/c5tv3/
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        方法：排序
        """
        # [[1,3],[2,6],[8,10],[15,18]]
        # [[1,4],[4,5]]
        # [[1,2],[3,4]]
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for curr in intervals[1:]:
            if curr[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], curr[1])
            else:
                result.append(curr)
        return result


s = Solution()

assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert s.merge([[1, 4], [4, 5]]) == [[1, 5]]
