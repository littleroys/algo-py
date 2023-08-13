from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                return True 
        return False


if __name__ == "__main__":
    pass
