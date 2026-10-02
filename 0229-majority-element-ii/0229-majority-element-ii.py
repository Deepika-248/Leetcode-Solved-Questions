class Solution(object):
    def majorityElement(self, nums):
        freq={}
        result=[]
        for ch in nums:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        for i in freq:
            if freq[i]>len(nums)//3:
                result.append(i)
        return result 