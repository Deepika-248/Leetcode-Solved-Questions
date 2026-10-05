class Solution(object):
    def maxDepth(self, s):
        count=0
        maximum=0
        for ch in s:
            if ch=='(':
                count+=1
                maximum=max(count,maximum)
            elif ch==')':
                count-=1
        return maximum