
from typing import List
from collections import Counter

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        count = Counter(nums)
        dup_num = miss_num = -1
        for i in range(1, len(nums) + 1):
            if count[i] == 2:
                dup_num = i
            elif count[i] == 0:
                miss_num = i
        return [dup_num, miss_num]

"""
找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
"""