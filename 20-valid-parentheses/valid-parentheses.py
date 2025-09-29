class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        length = len(s)

        for i in range(length):
            if stack and s[i] in dict and stack[-1] == dict[s[i]]:
                stack.pop()
            else:
                stack.append(s[i])
        isEmpty = not bool(stack)
        return isEmpty

        