class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        if len(s) == 0:
            return True
        while l < r:
            if s[l].lower().isalnum():
                if s[r].lower().isalnum():
                    if s[l].lower() == s[r].lower():
                        l += 1
                        r -= 1
                    else:
                        return False
                else:
                    r -= 1
            else:
                l += 1
        return True
        