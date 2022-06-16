class Solution:
    def isPalindrome(self, s: str) -> bool:
        foo = "".join(list(filter(str.isalnum, s.lower())))
        x,y = divmod(len(foo),2)
        if(foo[:x+y] == foo[x:][::-1]):
            return True
        return False

baz = ";;;rAcEcar"
foo = Solution()
print(foo.isPalindrome(baz))

baz = "bazzab"
foo = Solution()
print(foo.isPalindrome(baz))
