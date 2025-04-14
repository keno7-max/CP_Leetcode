def isBadVersion(version: int) -> bool:
    return version >= n


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left

# Example usage:
n = 5 
first_bad_version = 4  
isBadVersion = lambda version: version >= first_bad_version

solution = Solution()
result = solution.firstBadVersion(n)
print(f"The first bad version is: {result}")