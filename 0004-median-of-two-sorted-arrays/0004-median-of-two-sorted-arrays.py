class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left,right = 0,0
        output = []
        while left < len(nums1) and right < len(nums2):
            if nums1[left] <= nums2[right]:
                output.append(nums1[left])
                left += 1
            elif nums1[left] > nums2[right]:
                output.append(nums2[right])
                right += 1
        while left < len(nums1):
            output.append(nums1[left])
            left += 1
        while right < len(nums2):
            output.append(nums2[right])
            right += 1
        length = len(output)
        if length % 2 == 0:
            return (output[length//2 - 1] + output[length//2]) / 2
        else:
            return output[length//2]