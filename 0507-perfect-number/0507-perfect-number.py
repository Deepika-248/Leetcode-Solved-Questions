class Solution(object):
    def checkPerfectNumber(self, num):
        if num<=1:
            return False
        ori_num=num
        sum=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                sum=sum+i
                sum=sum+num//i
        if sum==ori_num:
            return True
        else:
            return False
        