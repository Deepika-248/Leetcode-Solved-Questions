class Solution(object):
    def isPalindrome(self, s):
        new_s=""
        for ch in s:
            if ch.isalnum():
                new_s=new_s+ch.lower()
        if new_s==new_s[::-1]:
            return True
        else:
            return False
        