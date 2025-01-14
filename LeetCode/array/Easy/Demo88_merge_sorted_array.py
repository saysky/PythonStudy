class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # 2 4 6
        # 1 3 5
        i, j = m - 1, n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # 3
        # 4 5 6
        # while i >= 0:
        #     nums1[k] = nums1[i]
        #     i -= 1
        #     k -= 1

        # 只需处理剩余的nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
