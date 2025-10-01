from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        queue = []
        result = 0
        i = 0
        while i < length:
            if not queue:
                queue.append(s[i])
            elif queue[0] == s[i]:
                queue.append(s[i])
                queue.pop(0)
            elif s[i] not in queue:
                queue.append(s[i])
            elif s[i] in queue:
                if result < len(queue):
                    result = len(queue)
                while queue[0] != s[i]:
                    queue.pop(0)
                i=i-1
            
            if i+1 < length and s[i] == s[i+1]:
                if result < len(queue):
                    result = len(queue)
                queue.clear()
            i=i+1

        if result < len(queue):
            result = len(queue)
        return result


           