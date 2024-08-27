class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        i = 1

        while i < len(nums):
            # increment i until you get a number that isnt a duplicate
            if nums[start] == nums[i]:
                i += 1
            # no duplicate so move start by one and swap then increment i
            else:
                start += 1
                nums[start] = nums[i]
                i += 1
        
        return start + 1
            
