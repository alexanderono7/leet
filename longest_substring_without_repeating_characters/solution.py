class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(s == None):
            return None
        max_length = 1
        current = ""
        for a in s:
            if a in current:
                if(max_length < len(current)):
                    max_length = len(current)
                current = current[1:]
            current += a
            print(current)
        if(max_length < len(current)):
            max_length = len(current)
        return max_length

        
foo = Solution()
print(foo.lengthOfLongestSubstring("banana"))
print(foo.lengthOfLongestSubstring("bbbbbb"))
print(foo.lengthOfLongestSubstring("abcabcbb"))
print(foo.lengthOfLongestSubstring("pwwkew"))
