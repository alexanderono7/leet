import random

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.lower = -pow(10,6)
        self.upper = pow(10,6)
        result = self.binSearch(nums1, nums2)
        if(result != "none"):
            return result
        else:
            result = self.binSearch(nums1, nums2)
            return result


    # Binary search nums1 for true median
    def binSearch(self, nums1, nums2):
        a = 0
        b = len(nums1)-1
        m = (a+b) // 2
        pos = (len(nums1)+len(nums2))//2 - m + 1
        while(a <= b):
            result = self.placement(nums1[m],pos,nums2)
            if(result == 2):
                return nums1[m]
            elif(result == 0):
                a = m + 1
            elif(result == 1):
                b = m - 1
        return "none"

    # 0 = x is too small to fit
    # 1 = x is too large to fit
    # 2 = x fits
    def placement(self, x, pos, nums):
        if(pos < 0):
            return 1
        elif( pos > len(nums)):
            return 0
        elif(pos == 0 and x <= nums[0]):
            return 2
        elif(pos == len(nums) and x >= nums[-1]):
            return 2
        elif(x >= nums[pos-1]):
            if(x <= nums[pos]):
                return 2
            else:
                return 1
        else:
            return 0

# 0 = x is too small to fit
# 1 = x is too large to fit
# 2 = x fits

nums = []
nums.sort()
print(nums)
x = 0
y = 0
print("x: " + str(x))
print("y: " + str(y))
foo = Solution()
print(foo.findMedianSortedArrays([1,3],[2]))
