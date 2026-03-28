class Solution:
    def isValid(self, s: str) -> bool:
        c = 0
        stack = []
        d = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        for i in s:
            if i in d.keys():
                stack.append(i)
                c += 1
            else:
                c -= 1
                if len(stack) != 0 and i == d.get(stack[-1]):
                    stack.pop()
        return len(stack) == 0 and c == 0