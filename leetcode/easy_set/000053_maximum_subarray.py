##########
#Question#
##########
'''
URL: https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-2147483647]
Output: -2147483647
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1

'''


##########
#Solution#
##########

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max=0
        global_max= (-2**31) -1
        
        for i in range(0,len(nums)):
            local_max = max(nums[i], nums[i]+local_max)
            
            if local_max > global_max:
                global_max = local_max
        
        return global_max
    
    def maxSubArray2(nums):
        final_sum = float("-inf")
        prevSum = 0
        print(nums)
        for num in nums:
            if prevSum < 0:
                prevSum = num
            else:
                prevSum += num

            final_sum = max(final_sum, prevSum)

        return final_sum

# [ 1 , 2, 3, 4,-1,-2, 55]
