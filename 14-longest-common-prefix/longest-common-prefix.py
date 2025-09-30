class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lengthfirst = len(strs[0])
        length = len(strs)
        count = 0

        if length == 1:
            return strs[0]
        
        for i in range(lengthfirst):
            temp=0
            for j in range(1,length):
                if i >= len(strs[j]):
                    return strs[0][0:count]
                if strs[0][i] != strs[j][i]:
                    temp=0
                    if strs[0] == "":
                        return ""
                    return strs[0][0:count]
                else:
                    temp=1

            count=count+temp
        
        return strs[0][0:count]
                    
                    
            

        