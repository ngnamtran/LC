class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        m = len(nums)
        summ = m*(m+1)/2
        return summ-sum(nums)
