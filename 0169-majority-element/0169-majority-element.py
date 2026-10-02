class Solution(object):
    def majorityElement(self, nums):
        freq={}
        for ch in nums:
            if ch in freq:
                freq[ch]=freq[ch]+1
            else:
                freq[ch]=1
        for i in freq:
            if freq[i]>len(nums)//2:
                return i
        