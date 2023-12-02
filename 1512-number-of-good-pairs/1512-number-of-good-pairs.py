class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        numbers_count = {}
        for item in nums:
            temp = numbers_count.get(item,0)
            good_pairs += temp
            numbers_count[item] = temp + 1
        return good_pairs