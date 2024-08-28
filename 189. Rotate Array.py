class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        #1 2 3 4 5 6 7 
        # 7 6 5 4 3 2 1
        # 7 6 5 | 4 3 2 1
        # 5 6 7 | 1 2 3 4
        nums.reverse()

        #handles cases where k is larger than size
        k %= len(nums)
        x = 0
        start = 0
        end = k - 1



        # re-reverse first half while x < k and while not in the middle index
        while (x < k and start < end):
            nums[start], nums[end] = nums[end], nums[start]
            x += 1
            start += 1
            end -= 1
        
        start = k
        end = len(nums) - 1

        # re-reverse second half
        while (x < len(nums) and start < end):
            nums[start], nums[end] = nums[end], nums[start]
            x += 1
            start += 1
            end -= 1
