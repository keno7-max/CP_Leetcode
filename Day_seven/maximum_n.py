class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        return max(sentence.count(' ') + 1 for sentence in sentences)
    


# Example usage:
solution = Solution()
result = solution.mostWordsFound(["Hello world", "My name is John", "I love programming"])
print(result)  