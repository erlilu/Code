from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        nums1 = []      # 奇数
        nums2 = []      # 偶数
        res = []
        for num in nums:
            if num % 2 == 0:
                nums2.append(num)
            else:
                nums1.append(num)
        for i in range(len(nums1)):
            res.append(nums2[i])
            res.append(nums1[i])
        return res



"""
给定一个非负整数数组 nums，  nums 中一半整数是 奇数 ，一半整数是 偶数 
"""