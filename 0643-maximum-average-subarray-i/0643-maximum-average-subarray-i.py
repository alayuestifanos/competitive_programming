class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum=0
        
        for i in range(k):
            maxSum += nums[i]
        tempSum=maxSum
            
        for i in range(k,len(nums)):
            tempSum=tempSum-nums[i-k]+nums[i]
            maxSum=max(maxSum,tempSum)
        return maxSum/k