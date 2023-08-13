class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        if len(a) <= len(b):
            a = "0" * (len(b) - len(a)) + a
        else:
            b = "0" * (len(a) - len(b)) + b
        i = max(len(a), len(b)) - 1
        carry = 0
        while i >= 0:
            sum = carry + int(a[i]) + int(b[i])
            carry = sum // 2
            result = str(sum % 2) + result
            i -= 1
        return result if carry == 0 else "1" + result


if __name__ == "__main__":
    s = Solution()
    assert "100" == s.addBinary("11", "1")
    assert "10101" == s.addBinary("1010", "1011")
