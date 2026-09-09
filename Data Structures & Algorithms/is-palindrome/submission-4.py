class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.translate(str.maketrans("", "", "@#!? ,';*&(%^)$~[{/.><-+}]:"))
        n = len(s)
        d = n//2
        s1 = s[:d]
        if n % 2 != 0:
            # o = n//2
            s2 = "".join(reversed(s[d+1:]))
        else:
            s2 = "".join(reversed(s[d:]))
        if s1 == s2:
            return True
        else:
            return False