#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 02:22:18 2022

@author: shivengoyal
"""


"""
Search Insert Position
Easy

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # SOLUTION 1 - BRUTE FORCE
        """
        if(target < nums[0]):
            return 0
        if(target > nums[len(nums)-1]):
            return len(nums)
        for i in range(0, len(nums)):
            if(nums[i] == target):
                return i
            else:
                if(nums[i] > target):
                    return i
        """
            
        # SOLUTION 2 - O(log n)
        min = 0
        max = len(nums) - 1
        
        while(min <= max):
            
            mid = (min+max)//2
            if(nums[mid] == target):
                return mid
            else:
                if (target > nums[mid]):
                    min = mid+1
                else:
                    max = mid-1
        return min