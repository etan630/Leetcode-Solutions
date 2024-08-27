#easy
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        end = m + n - 1
        
        while (j >= 0):
            if (i >= 0 and nums1[i] > nums2[j]):
                nums1[end] = nums1[i]
                i -= 1
                end -= 1
            else:
                nums1[end] = nums2[j]
                j -= 1
                end -= 1

        # you don't actually need this part
        while (i > 0):
            nums1[end] = nums1[i]
            i -= 1
            end -= 1
        
        while (j > 0):
            nums1[end] = nums2[j]
            j -= 1
            end -= 1
        

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
