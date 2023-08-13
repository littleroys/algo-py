from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                counter.pop(n)
        target, _ = counter.popitem()
        return target

    def singleNumber1(self, nums: List[int]) -> int:
        """
        XOR same number it wil return zero
        """
        return reduce(lambda total, num: total ^ num, nums)


if __name__ == "__main__":
    l1 = [4, 1, 2, 1, 2]
    s = Solution()
    res = s.singleNumber(l1)
    print(res)
    res1 = s.singleNumber1(l1)
    print(res1)
