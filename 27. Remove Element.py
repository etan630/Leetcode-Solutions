class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        end = len(nums) - 1
        start = 0

        while start <= end:
            # move to end and decrement end... if it is still val itll 
            # continue to swap and decrease end
            if nums[start] == val:
                nums[start] = nums[end]
                end -= 1
            else:
                start += 1

        return start
