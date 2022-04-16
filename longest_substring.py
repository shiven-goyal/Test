#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 17:58:40 2022

@author: shivengoyal
"""

"""
3. Longest Substring Without Repeating Characters
Medium


Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # SOLUTION 1 - BRUTE FORCE, Time Complexity - O(n^2), Space - O(n)
        """
        max_length = 0
        string = ""
        
        for i in range(0, len(s) + 1):
            for j in range(i+1, len(s) + 1):
                string = s[i:j]
                
                if (len(string) == len(set(string)) and len(string) > max_length):
                    
                    max_length = len(string)
                    
        return max_length
        """
        
        # SOLUTION 2 - DYNAMIC PROGRAMING
        
        dict = {}
        max_length = 0
        start = 0
        
        for i in range(0, len(s)):
            
            if s[i] in dict:
                start = max(start, dict[s[i]] + 1)
            
            dict[s[i]] = i
            
            max_length = max(max_length, i - start +1)
            
        return max_length
                
            