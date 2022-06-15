from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''Given two sorted arrays, return the median value if both arrays were combined (in O(log(n+m)) time).'''
        n = len(nums1)
        m = len(nums2)
        target = int((n+m)/2)
        if((n+m) % 2 != 0): odd = True
        else: odd = False
        return None

    def indexSearch(self, foo, bar, a, b):
        '''Search the list 'foo'[a:b] for an element which is greater than or equal to half of elements in
        a sorted combined list of foo and bar'''
        total = len(foo) + len(bar) # Get length of combined list
        d = int((a+b)/2)            # d   = median index of foo[a:b] subsection
        med = foo[d]                # med = median value of foo[a:b] subsection
        c = int(total/2) - d - 1    # c = corresponding index in 'bar' to 'd' in 'foo'
        while(1):
            if(c - 1 in range(len(bar))):
                if(med <= bar[c] and med >= bar[c-1]):
                    return d
        return c


        
foo = [1,2,3,4,5]
bar = [6,7,8,9,10]
baz = Solution()
baz.indexSearch(foo, bar, 0, len(foo))
