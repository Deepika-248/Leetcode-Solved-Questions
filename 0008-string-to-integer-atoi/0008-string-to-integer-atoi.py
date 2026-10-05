class Solution(object):
    def myAtoi(self, s):
        s=s.strip()
        if not s:
            return 0
        i=0
        sign=1
        if s[i]=='-' or s[i]=='+':
            sign= -1 if s[i]=='-' else 1
            i+=1
        num=0
        while i<len(s) and s[i].isdigit():
            num=num*10+int(s[i])
            if num*sign>2147483647:
                return 2147483647
            if num*sign<-2147483648:
                return -2147483648
            i+=1
        return num*sign
        