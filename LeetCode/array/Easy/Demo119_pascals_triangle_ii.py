class Solution(object):
    def getRow(self, rowIndex):
        """
        杨辉三角II
        :type rowIndex: int
        :rtype: List[int]
        """
        # result = []
        # for i in range(rowIndex+1):
        #     temp = [1] * (i + 1)
        #     for j in range(1, i):
        #         temp[j] = result[i-1][j-1] + result[i-1][j]
        #     result.append(temp)
        # return result[-1]

        # n = rowIndex + 1
        # result = [1] * (n)
        # for i in range(n):
        #     temp = list(result)
        #     for j in range(1, i):
        #         result[j] = temp[j-1] + temp[j]
        #     del temp
        # return result

        n = rowIndex + 1
        result = [1] * n
        for i in range(2, n):
            for j in range(i - 1, 0, -1):  # 从右往左，从i-1 到 0，不包括0
                result[j] += result[j - 1]
        return result
