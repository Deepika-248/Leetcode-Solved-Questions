class Solution(object):
    def isPalindrome(self, x):
        
        ori_num=x
        reverse=0
        while x>0:
            last_digit=x%10
            reverse=reverse*10+last_digit
            x=x//10
        #reverse=reverse*sign
        if ori_num==reverse:
            return True
        else:
            return False
        