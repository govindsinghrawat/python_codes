##########
#Question#
##########
'''
URL: https://leetcode.com/problems/contains-duplicate-ii/

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

'''


##########
#Solution#
##########

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices_nums = {}
        
#         for i in range(k, len(nums)):
#             for j in range(0, len(nums)-k):
#                 if nums[j] == nums[j+k]:
#                     return True
                
#         return False
        
        for i in range(len(nums)):
            if nums[i] in indices_nums.keys():
                indices_nums[nums[i]].append(i)
            else:
                indices_nums[nums[i]] = [ i ]

        for _, value_list in indices_nums.items():
            if len(value_list) > 1:
                for j in range(len(value_list)-1):
                    if abs(value_list[j] - value_list[j+1]) <= k:
                        return True

        return False
                
