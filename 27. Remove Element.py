class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        end = len(nums) - 1
        k = 0
        start = 0

        while start < end:
            # if end has val go down by one
            if nums[end] == val:
                end -= 1
                k += 1
            # if start has val and end doesnt, put end into start then move on
            if nums[start] == val and nums[end] != val:
                nums[start] = nums[end]
                start += 1
                end -= 1
                k += 1
            else:
                start += 1
            

        return len(nums) - k
