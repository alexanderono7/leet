import re
class Solution:
    def myAtoi(self, s: str) -> int:
        match = re.match(r'\s*((-|\+)?\d+)', s)
        if(match == None):
            return 0
        match = int(match.group(0))
        if(match > (2**31 - 1)):
            return 2**31 - 1
        if(match < (-2**31)):
            return -2**31
        return match

foo = Solution()
print("========================================")
print(foo.myAtoi("banana--123obama"))
print(foo.myAtoi("42"))
print(foo.myAtoi("        -42"))
print(foo.myAtoi("4193 with words"))
print(foo.myAtoi("+1"))
