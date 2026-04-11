class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        l = 0
        for i in s:
            if (i - 1) not in s:
                c = i
                c_total = 1

                while (c + 1) in s:
                    c += 1
                    c_total += 1
                l = max(l, c_total)
        return l