class Solution:
    def maxArea(self, height) -> int:
        a = 0
        b = len(height) - 1
        maxA = height[a]
        maxB = height[b]
        width = b - a
        maxArea = (width * min(height[a], height[b]))
        while(a < b):
            print(f"a:{a},b:{b}")
            print(f"aval:{height[a]},bval:{height[b]}")
            if(height[a] != height[b]):
                print("tag")
                # Iterate shorter pointer until a new personal highest point is found.
                if(height[a] < height[b]):
                    original = height[a]
                    while(height[a] <= original and a < b):
                        a += 1
                else:    
                    original = height[b]
                    while(height[b] <= original and a < b):
                        b -= 1
            else:
                a += 1
                b -= 1
            width = b - a
            maxArea = max(maxArea, (width * min(height[a], height[b])))
            maxA = max(maxA, height[a])
            maxB = max(maxB, height[b])
            #exit(0)
        return maxArea

foo = Solution()
testcases = [
[1,8,6,2,5,4,8,3,7]
]

for x in testcases:
    print(foo.maxArea(x))
