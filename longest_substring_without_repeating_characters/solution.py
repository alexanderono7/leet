import timeit

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(s == None):
            return None
        max_length = 0
        current = ""
        lengths = []
        for a in s:
            try:
                position = current.index(a)+1
                lengths.append(len(current))
                current = current[current.index(a)+1:]
            except: pass
            current += a
        lengths.append(len(current))
        return max(lengths)

        
foo = Solution()
start = timeit.default_timer()
print(foo.lengthOfLongestSubstring("banana"))
print(foo.lengthOfLongestSubstring("bbbbbb"))
print(foo.lengthOfLongestSubstring("abcabcbb"))
print(foo.lengthOfLongestSubstring("pwwkew"))
stop = timeit.default_timer()
print("Time: ", stop - start)
