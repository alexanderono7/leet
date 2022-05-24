from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''Given two sorted arrays, return the median value if both arrays were combined (in O(log(n+m)) time).'''
    n = len(nums1)
    m = len(nums2)
    target = int((n+m)/2)
    if((n+m) % 2 != 0): odd = True
    else: odd = False

    def indexSearch(nums, x, a, b):
        '''Return the # of elements that are less than/equal to 'x' in 'nums'[a:b], 
        where 'nums' is a sorted list of integers.  Uses binary search.'''
        med = int((a+b)/2)
        c = nums[med] # Get median value of subsection
        while():
            if(x > nums[c]):
                a = med+1
            else:
                b = med

            c = nums[med]
        return c




        

        
