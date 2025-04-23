class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count
        


# Example usage:
solution = Solution()
result = solution.trailingZeroes(100)
print(result)  