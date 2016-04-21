class Solution(object):
  def countBits(self, num):
    countOneList = []
    for i in range(0, num+1):
      binaryStr = "{0:b}".format(i)
      countOneList.append(binaryStr.count("1"))
    return countOneList

# Test Case
sol = Solution()
print sol.countBits(5)

# Ideas
# convert int to binary string and count the number of ones
