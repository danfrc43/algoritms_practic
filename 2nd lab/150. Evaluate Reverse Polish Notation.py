class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for i in tokens:
            if i == "+":
                res.append(res.pop() + res.pop())
            elif i == "-":
                s, f = res.pop(), res.pop()
                res.append(f - s)
            elif i == "*":
                res.append(res.pop() * res.pop())
            elif i == "/":
                s, f = res.pop(), res.pop()
                res.append(int(f / s))
            else:
                res.append(int(i))
        return res[0]