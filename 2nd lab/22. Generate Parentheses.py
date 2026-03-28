class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = [(0, 0, '')]
        while stack:
            l, r, s = stack.pop()    
            if len(s) == n * 2:
                res.append(s)
                continue           
            if l < n:
                stack.append((l + 1, r, s + '('))           
            if r < l:
                stack.append((l, r + 1, s + ')'))
        return res
