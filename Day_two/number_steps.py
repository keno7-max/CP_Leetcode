class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num > 0 :
            if num % 2 == 0 :
                num = num // 2
            else :
                num -= 1
            steps += 1
        return steps
    

# Example usage:
solution = Solution()
result = solution.numberOfSteps(14)
print(result)  # Output: 6 (14 -> 7 -> 6 -> 3 -> 2 -> 1 -> 0)