from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        n = len(digits)
        # 去重
        res_set = set()

        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if digits[k] % 2 == 0:          # 个位是偶数
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        res_set.add(num)

        return sorted(res_set)