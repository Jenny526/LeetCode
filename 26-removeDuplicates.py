__author__ = 'jintao'

class Solution:
    def removeDuplicates(self, A):
        count = 0
        if(len(A) <=1):
            return len(A)
        for index in range(0, len(A)):
            if(A[count] != A[index]):
                temp = A[index]
                A[index] = A[count+1]
                A[count+1] = temp
                count += 1

        return count+1

# Test Case
sol = Solution()
print sol.removeDuplicates([1,2,3,3,4,4,5])

# Ideas
# this problem only counts the number of different items
# so, it should be easier
