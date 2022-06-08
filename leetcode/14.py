class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs)==1:
            return strs[0]
        else:
            flag=False
            if "" in strs:
                return ""
            else:
                for i in range(len(strs)-1,0,-1):
                    if strs[i]<strs[i-1]:
                        strs[i],strs[i-1] = strs[i-1],strs[i]
                # 把最短的字符放到最前面
                for j in range(len(strs[0])):
                    a=strs[0][j]
                    # return a
                    for i in range(len(strs)):
                        if strs[i][j]!=a:
                            flag=True 
                            break
                    if flag:
                        return strs[0][:j]
                        break
                if flag==False:
                    return strs[0]