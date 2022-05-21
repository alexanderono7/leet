import re
class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.match(r'\s*(-?\d+)', s)
        if(match == None):
            return None
        match = int(match.group(1))
        if(match > (2**31 - 1)):
            return 2**31 - 1
        if(match < (-2**31)):
            return -2**31
        return match

foo = Solution()
print("========================================")
(foo.myAtoi("banana--123obama"))
(foo.myAtoi("42"))
(foo.myAtoi("        -42"))
(foo.myAtoi("4193 with words"))
