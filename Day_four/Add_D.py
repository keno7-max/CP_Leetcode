class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
           return 0
        return 1 + (num - 1) % 9
    

# Example usage:
solution = Solution()
num = 39
result = solution.addDigits(num)
print(result)



