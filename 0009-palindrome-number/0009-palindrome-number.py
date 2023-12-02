class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if(x>=0):
        #     num=int(str(x)[::-1])
        #     if(num == x):
        #         return True
        #     return False
        # else:
        #     return False
        if x < 0:
            return False
        numString = str(x)
        left = 0
        right = len(numString)-1
        while left < right:
            if numString[left] != numString[right]:
                return False
            left += 1
            right -= 1
        return True