"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example - 
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class TwoSum:
    def two_sum(self, nums, target):
        """
        Create a dictionary and save key value pairs for each
        element
        Loop through the list and add element-index pair in 
        dictionary. If target - element is already there in
        dictionary, return the index of element and the value
        fetched from dict.
        Time complexity = O(n) as list traverse for each element
        is done only once.
        Space complexity = O(n) due to dict storage
        """
        result = {}
        for index, element in enumerate(nums):
            if target - element in result:
                return [result[target - element], index]
            else:
                result[element] = index


