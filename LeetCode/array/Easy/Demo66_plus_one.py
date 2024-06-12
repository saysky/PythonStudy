class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # temp = digits[::-1]
        # c = 1
        # for i in range(len(temp)):
        #     if temp[i] + c >= 10:
        #         c = 1
        #         temp[i] = 0  # 需要进位
        #     else:
        #         temp[i] += c  # 不需要进位
        #         c = 0
        # if c == 1:
        #     temp.append(1)
        # return temp[::-1]

        carry = 1
        for i in reversed(range(len(digits))):
            sum = digits[i] + carry
            carry = sum // 10
            digits[i] = sum % 10
            if carry == 0:
                break
        if carry == 1:
            digits.insert(0, 1)
        return digits
