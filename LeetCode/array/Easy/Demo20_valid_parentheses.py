class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == '[' or char == '{' or char == '(':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                out = stack.pop()
                if char == ']' and out != '[':
                    return False
                if char == '}' and out != '{':
                    return False
                if char == ')' and out != '(':
                    return False
        return len(stack) == 0  # not stack


solution = Solution()
print(solution.isValid('[[]]'))
