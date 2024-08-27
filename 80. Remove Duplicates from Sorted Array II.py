#medium
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        start = 1
        i = 2

        while i < len(nums):
            #essentially you want to look for next i if there was already two numbers
            if (nums[start] == nums[i] and nums[start - 1] == nums[start]):
                i += 1
            else:
                start += 1
                nums[start] = nums[i]
                i += 1

        return start + 1
