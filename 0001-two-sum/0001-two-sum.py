class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_count = {}
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in number_count:
                return [i,number_count[temp]]
            number_count[nums[i]] = i
        
 