class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # i = 0
        # c = 0
        # list1 = []
        # a = a[::-1]
        # b = b[::-1]
        # while i < len(a) and i < len(b):
        #     m = int(a[i]) + int(b[i]) + c
        #     if m >= 2:
        #         c = 1
        #         list1.append(m % 2)
        #     else:
        #         c = 0
        #         list1.append(m)
        #     i += 1
        #
        # while i < len(a):
        #     m = int(a[i]) + c
        #     if m >= 2:
        #         c = 1
        #         list1.append(m % 2)
        #     else:
        #         c = 0
        #         list1.append(m)
        #     i += 1
        #
        # while i < len(b):
        #     m = int(b[i]) + c
        #     if m >= 2:
        #         c = 1
        #         list1.append(m % 2)
        #     else:
        #         c = 0
        #         list1.append(m)
        #     i += 1
        #
        # if c == 1:
        #     list1.append(1)
        # return ''.join([str(x) for x in list1[::-1]])

        a_len, b_len = len(a), len(b)
        max_len = max(a_len, b_len)
        carry = 0
        result = []
        a = a[::-1]
        b = b[::-1]
        for i in range(max_len):
            curr_a = int(a[i]) if i < a_len else 0
            curr_b = int(b[i]) if i < b_len else 0
            sum = curr_a + curr_b + carry
            carry = sum // 2
            result.append(str(sum % 2))
        if carry == 1:
            result.append('1')
        return ''.join(result[::-1])
