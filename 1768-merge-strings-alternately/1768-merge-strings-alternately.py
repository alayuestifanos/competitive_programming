class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        left = 0
        right = 0
        output = ""
        while left < len(word1) and right < len(word2):
            output += word1[left]
            output += word2[right]
            left += 1
            right += 1
        
        while left < len(word1):
            output += word1[left]
            left += 1
        while right < len(word2):
            output += word2[right]
            right += 1
        return output