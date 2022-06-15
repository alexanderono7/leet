class Solution:
    def search(self, nums, target: int) -> int:
        a = 0
        b = len(nums)-1
        while(True):
            m = (b+a) >> 1 # m = median of nums[a:b]
            med = nums[m]
            print(nums[a:b])
            print("m:" + str(m))
            if(med == target):
                return m
            else:
                if(target < med):
                    b = m-1
                else:
                    a = m+1
            if(b-a < 1):
                return -1

foo = Solution()
foo.search([-1,0,3,5,9,12],9)
