import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles) - 1
        k = 10**9
        while l <= r:
            mid = (l + r) // 2
            sum_ks = 0
            for i in piles:
                sum_ks += math.ceil(i/(mid + 1))
            if sum_ks > h:
                l = mid + 1
            elif sum_ks <= h:
                k = min(k, mid + 1)
                r = mid - 1
        return k
