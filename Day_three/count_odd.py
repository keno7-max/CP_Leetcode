class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        return ((high + 1) // 2) - (low // 2)

# Example usage:
low = 3
high = 7
solution = Solution()
result = solution.countOdds(low, high)
print(result)  