##########
#Question#
##########
'''
URL: https://leetcode.com/problems/search-insert-position/
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104


'''


##########
#Solution#
##########
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
#         if nums[-1] < target:
#             return len(nums)
#         try:
#             return nums.index(target)
#         except ValueError:
            
#             for i in range(0,len(nums)):
#                 if nums[i] > target:
#                     break
#             return i
        if(target in nums):
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            ind = nums.index(target)
            return ind
