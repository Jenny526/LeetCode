class Solution(object):
  def canWinNim(sef, n):
    if n>3 and n % 4 == 0:
      return False
    else:
      return True

# Test Case
sol = Solution()
print sol.canWinNim(2)
print sol.canWinNim(4)
print sol.canWinNim(5)

# Ideas
# It is observed that whoever starts with 4k number of stones never wins

