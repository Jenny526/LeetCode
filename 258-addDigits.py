class Solution(object):
  def addDigits(self, num):
    reminder = num % 9
    if num == 0:
      return 0
    elif reminder == 0:
      return 9
    else:
      return reminder

# test case
sol = Solution()
print sol.addDigits(38)
print sol.addDigits(37)
print sol.addDigits(39)

# idea
# since the result only keeps one digit
# so the result must be in the range from 0 - 9
# therefore, the input and result observes a pattern
# num == 0 -> 0
# num = 9k + 1 -> 1
# num = 9k + 2 -> 2
# num = 9k + 3 -> 3
# num = 9k + 4 -> 4
# num = 9k + 5 -> 5
# num = 9k + 6 -> 6
# num = 9k + 7 -> 7
# num = 9k + 8 -> 8
# num = 9k     -> 9
