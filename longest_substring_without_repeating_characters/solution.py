import timeit

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(s == None):
            return None
        max_length = 0
        current = ""
        for a in s:
            try:
                if(max_length < len(current)): max_length = len(current)
                current = current[current.index(a)+1:]
            except: pass
            current += a
        if(max_length < len(current)): max_length = len(current)
        return max_length

        
foo = Solution()
start = timeit.default_timer()
print(foo.lengthOfLongestSubstring("banana"))
print(foo.lengthOfLongestSubstring("bbbbbb"))
print(foo.lengthOfLongestSubstring("abcabcbb"))
print(foo.lengthOfLongestSubstring("pwwkew"))
stop = timeit.default_timer()
print("Time: ", stop - start)
