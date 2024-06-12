class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(0, numRows):  # 0 1 2 3 4
            temp = [1] * (i + 1)
            for j in range(1, i):
                temp[j] = result[i - 1][j - 1] + result[i - 1][j]
            result.append(temp)
        return result
