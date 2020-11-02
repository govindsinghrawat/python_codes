##########
#Question#
##########
'''
URL: https://leetcode.com/problems/climbing-stairs/

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

'''


##########
#Solution#
##########
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=1:
            return 1
        
        x = [ 0 for i in range(n+2)]
                
        x[0] = 0
        x[1] = 1
        for i in range(2,n+2):
            x[i] = x[i-1]+x[i-2]
        
        return x[-1]
        

class Solution2:
    def climbStairs(self, n: int) -> int:
        num = [0,0]
        num[0] = 1
        num[1] = 2
        for i in range(2,n):
            num.append(num[i-1] + num[i-2])
        return num[n-1]
