class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        return len(words[-1]) if len(words) != 0 else 0


if __name__ == "__main__":
    s = Solution()
    test_str1 = "   fly me   to   the moon  "
    test_str2 = "    "
    assert 4 == s.lengthOfLastWord(test_str1)
    assert 0 == s.lengthOfLastWord(test_str2)
