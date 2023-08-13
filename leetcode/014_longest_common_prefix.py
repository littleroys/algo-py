from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
           pass   
        return result

        


if __name__ == "__main__":
    s = Solution()
    assert "fl" == s.longestCommonPrefix( ["flower","flow","flight"])
    assert "" == s.longestCommonPrefix( ["dog","racecar","car"])

