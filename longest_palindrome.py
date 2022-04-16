#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 00:08:18 2022

@author: shivengoyal
"""

"""
5. Longest Palindromic Substring
Medium

Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
    
        # SOLUTION 1 - BRUTE FORCE 
        
        """
        max_length = 0
        reverse = ""
        string = ""
        
        dict = {}
        
        for i in range(0, len(s) + 1):
            for j in range(i+1, len(s) + 1):
                
                string = s[i:j]
                reverse = string[::-1]
                
                if (string == reverse and len(string) > max_length):
                    
                    max_length = len(string)
                    dict[max_length] = string
                    
        for key,value in dict.items():
            if(key==max_length):
                return value
                
         """  
        # HOW TO FIND A PALINDROME
        
        """
        len_string = len(s)
        start = 0
        end = len(s)-1
        
        while(start <= (len(s) - 1)//2 and end >= len(s)//2 ):
            
            if(s[start] == s[end]):
                start=start+1
                end=end-1
            
            else:
                return(False)
        return(True)
        """
        
        # SOLUTION 2 - Dynamic Programming
        
        max_palindrome = ""
        left = 0
        right = 0
        
        
        if len(s) == 0:
            return s
        if len(s) == 1:
            return s
        if len(set(s)) == 1:
            return s
        
        
        for i in range(0, len(s) - 1):
            if (s[i] == s[i+1]):            # even condition
                
                left = i
                right = i + 1
                
                while(left > 0 and right < len(s)-1):
                    
                    if(s[left-1] == s[right+1]):
                        left = left - 1
                        right = right + 1
                    else:
                        break
                 
                string = s[left:right+1]
                if(len(string) > len(max_palindrome)):
                    max_palindrome = string
            
                    
                    
            if (i>0 and s[i-1] == s[i+1]):      # odd condition
                left = i-1
                right = i+1
                
                while(left>0 and right < len(s) - 1):
                    
                    if(s[left-1] == s[right+1]):
                        left = left - 1
                        right = right + 1
                    else:
                        break
                        
                string = s[left:right+1]
                if(len(string) > len(max_palindrome)):
                    max_palindrome = string
                
        if max_palindrome == "":
            return s[0]
        else:
            return max_palindrome
            
        
                        
    
        
            
        