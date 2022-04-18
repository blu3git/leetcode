"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should 
be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example - 
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""

class MergeSortedArray:

    def merge(self, nums1, m, nums2, n):
        """
        Time complexity: O(m+n).

        We are performing n+2⋅m reads and n+2⋅m writes. Because constants are 
        ignored in Big O notation, this gives us a time complexity of O(n+m).

        Space Complexity: O(1)
        
        """
        if n==0:
            pass
        else:
            i = m -1
            j = n-1
            for k in range(n+m-1, -1, -1):
                if j < 0: break
                if i >= 0 and nums1[i] > nums2[j]:
                    nums1[k] = nums1[i]
                    i = i-1
                else:
                    nums1[k] = nums2[j]
                    j = j-1

        print(nums1)

if __name__ == "__main__":
    #MergeSortedArray().merge([1,2,3,0,0,0], 3, [2,5,6], 3)
    #MergeSortedArray().merge([1], 1, [], 0)
    #MergeSortedArray().merge([0], 0, [1], 1)
    #MergeSortedArray().merge([2,0], 1, [1], 1)
    MergeSortedArray().merge([4,5,6,0,0,0], 3, [1,2,3], 3)