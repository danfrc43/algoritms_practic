class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = [0] * 20001
        for num in nums:
            c[10000 + num] += 1
        res = []
        while len(res) < k:
            res.append(c.index(max(c)) - 10000)
            c[c.index(max(c))] = 0
        return res