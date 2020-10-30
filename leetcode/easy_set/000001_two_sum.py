##########
#Question#
##########
'''
URL: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109

Only one valid answer exists.
'''


##########
#Solution#
##########


import itertools
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        result = []
        for i in range(0,len(nums)):
            if nums[i] in index_map.keys():
                # index_map[nums[i]] = [i]
                index_map[nums[i]].append(i)
            else:
                index_map[nums[i]] = [i]
            #print(index_map)
        
        for (a,b) in itertools.combinations(nums, 2):
            if a+b == target:
                #print(index_map[a], index_map[b])
                if a==b:
                    result.append(index_map[a][0])
                    result.append(index_map[a][1])
                else:
                    result.append(index_map[a][0])
                    result.append(index_map[b][0])
                break;
    
        return result
                

