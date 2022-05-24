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
        '''Return the # of elements that are less than 'x' in 'nums'[a:b], where 'nums' is a sorted list of integers (the index if x were inserted, essentially).
        Implements binary search.'''
        med = int((a+b)/2)
        c = nums[med] # Get median value of subsection
        if(x < nums[c]):
            indexSearch(nums, x, a, med)
        elif(x > nums[c]):
            indexSearch(nums, x, med, b)
        else:
            return c




        

        
