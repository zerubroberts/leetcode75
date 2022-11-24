
from typing import List

class Solution:
    def pivotIndex(self, nums:List[int]) -> int:

        #create list with cumulative sum
        nums_cumsum = []
        counter=0
        for i,n in enumerate(nums):
            counter = counter+n
            nums_cumsum.append(counter)

        #same as above - but reverse
        nums_cumsum_reverse = []
        counter=0
        for i,n in enumerate(nums[::-1]):
            counter = counter+n
            nums_cumsum_reverse.append(counter)
        
        #reverse it again
        nums_cumsum_reverse = nums_cumsum_reverse[::-1]

        #find the index where the two sums match
        for i,j in enumerate(nums_cumsum):
            if nums_cumsum[i] == nums_cumsum_reverse[i]:
                return i
                break
        else:
            return -1


#this is a test for commit

myclass = Solution()
print(myclass.pivotIndex([1,7,3,6,5,6]))

if __name__ == '__main__':
    pass
