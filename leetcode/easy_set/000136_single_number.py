##########
#Question#
##########
'''
URL: https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

'''


##########
#Solution#
##########

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         odd_sum=0
#         even_sum=0
#         for i in range(len(nums)):
#             if i%2:
#                 odd_sum+=nums[i]
#             else:
#                 even_sum+=nums[i]
                
#         return even_sum-odd_sum
        
        a = 0
        for n in nums:
            a = a ^ n
        return a
