#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 00:43:40 2022

@author: shivengoyal
"""

def merge_sorted_arrays(arr1, arr2):
    i=0
    j=0
    sorted_list = []
    
    while(i < len(arr1) and j < len(arr2)):
        if (arr1[i] > arr2[j]):
            sorted_list.append(arr2[j])
            j = j+1
        else:
            sorted_list.append(arr1[i])
            i = i+1
    
    if (i < len(arr1)):
        for x in range(i, len(arr1)):
            sorted_list.append(arr1[x])
    if (j < len(arr2)):
        for y in range(j, len(arr2)):
            sorted_list.append(arr2[y])
    
    return sorted_list
    
    
arr_one = [1,4,8,9]
arr_two = [0,9,11,89,90]

print("Sorted Array Is: ", merge_sorted_arrays(arr_one, arr_two))