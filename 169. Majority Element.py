#easy
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()

        # since each element appears more than n/2 time you 
        # could just find the element there
        return nums[len(nums) // 2]

        #alternative solution

        #start = 0
        #i = 0
        #count = 0
        #k = nums[0]

        # iterate i throughout the array
        #while i < len(nums):
            # count the number of times you would have to iterate
            # store current most occurance
            #if nums[start] == nums[i]:
                #i += 1
                #count += 1
                #k = nums[start]
            
            # move start to current position of i to check next
            #start = i
            #i += count

        #return k
