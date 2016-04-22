__author__ = 'jintao'

class Solution:
  # slower
  # add one in the original list
  def plusOne(self, digits):
    index = len(digits)-1
    plusOne = False
    
    while(index >=0):
      if(plusOne):
        digits[index] += 1
      plusOne = False
      if(index == len(digits)-1):
        digits[index] += 1
      if(digits[index] >= 10):
        plusOne = True
        digits[index] = 10 - digits[index]
      index -= 1
    if(plusOne):
      digits.insert(0,1)
    return digits

  # faster
  # convert list to int, and one, then get result as a list
  def plusOneV2(self, digits):
    base = 1
    num = 0
    for item in digits:
      num = num*10 + item
    num += 1
    digits = []
    while num >= 1:
      digits = [num%10] + digits
      num = num / 10
    return digits
# Test Case 
sol = Solution()
print sol.plusOne([1,9,9])
print sol.plusOne([9])
print sol.plusOneV2([1,9,9])
print sol.plusOneV2([9])

# Ideas
# one way is to do add one on the original list
# another way is to convert list to int, then add one
