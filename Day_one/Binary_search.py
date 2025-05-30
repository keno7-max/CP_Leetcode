class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2 
            if nums[mid] == target:
                return mid  
            elif nums[mid] < target:
                left = mid + 1  
            else:
                right = mid - 1  

        return -1  

# Example usage:
nums = [-1, 0, 3, 5, 9, 12]
target = 9
solution = Solution()
result = solution.search(nums, target)
print(result) 