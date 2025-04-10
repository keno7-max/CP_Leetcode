# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
       
        while low <= high :
            mid = (low + high) // 2
            if guess(mid) == 0 :
                return mid
            elif guess(mid) == -1 :
                high = mid - 1
            else :
                low = mid + 1

# Example usage:
def guess(num):
    secret_number = 2457654  
    if num < secret_number:
        return 1
    elif num > secret_number:
        return -1
    else:
        return 0
solution = Solution()
result = solution.guessNumber(1000000000000000)
print(result) 