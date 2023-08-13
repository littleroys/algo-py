class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        end = len(num_str)
        for i in range(end):
            if num_str[i] != num_str[end - i - 1]:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert True == s.isPalindrome(121)
    assert True == s.isPalindrome(123321)
    assert False == s.isPalindrome(-121)
    assert False == s.isPalindrome(10)
    assert False == s.isPalindrome(1000021)
