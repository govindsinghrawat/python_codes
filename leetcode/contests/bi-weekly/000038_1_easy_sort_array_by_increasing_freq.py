##########
#Question#
##########
'''
URL: https://leetcode.com/problems/sort-array-by-increasing-frequency/

Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
 

Constraints:

1 <= nums.length <= 100
-100 <= nums[i] <= 100
'''


##########
#Solution#
##########

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        freq_nums = {}
        for num in nums:
            freq_nums[num] = freq_nums.get(num, 0) + 1


        rev_freq_nums = {}
        for k,v in freq_nums.items():
            if v not in rev_freq_nums.keys():
                rev_freq_nums[v] = [k]
            else:
                rev_freq_nums[v].append(k)

        result = []
        for key, value in sorted(rev_freq_nums.items()):
            values= list(value)
            
            if len(values) == 1:    
                for item in values:
                    for i in range(0,key):
                        result.append(item)
            else:
                for item in sorted(values, reverse=True):
                    for i in range(0,key):
                        result.append(item)
        return result

