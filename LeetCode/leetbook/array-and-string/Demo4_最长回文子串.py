class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(str):
            if str[0] != str[-1]:
                return False
            return str == str[::-1]

        result = ''
        for i in range(len(s)):
            for j in range(i, len(s)):
                substr = s[i:j + 1]
                if isPalindrome(substr) and len(substr) > len(result):
                    result = substr
        return result


assert Solution().longestPalindrome("babad") == "bab"
