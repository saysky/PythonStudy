class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # if len(s) == 1:
        #     return value_dict[s[0]]
        #
        # for i in range(len(s) - 1):
        #     curr_value = value_dict[s[i]]
        #     next_value = value_dict[s[i + 1]]
        #     if curr_value < next_value:
        #         sum = sum - curr_value
        #     else:
        #         sum = sum + curr_value
        # sum = sum + value_dict[s[i + 1]]

        # IX => XI
        sum = 0
        prev_value = 0
        for char in reversed(s):
            curr_value = value_dict[char]
            if curr_value < prev_value:
                sum -= curr_value
            else:
                sum += curr_value
            prev_value = curr_value
        return sum
