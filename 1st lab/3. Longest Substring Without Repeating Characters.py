class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLenght = 0
        left = 0
        c = set()
        for right in range(n):
            if s[right] not in c:
                c.add(s[right])
                maxLenght = max(len(c), maxLenght)
            else:
                while s[right] in c:
                    c.remove(s[left])
                    left += 1
                c.add(s[right])
        return maxLenght

        