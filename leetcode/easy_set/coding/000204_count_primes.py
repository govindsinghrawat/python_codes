##########
#Question#
##########
'''
URL: https://leetcode.com/problems/count-primes/

Count the number of prime numbers less than a non-negative number, n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106

'''


##########
#Solution#
##########

class Solution:
    def countPrimes(self, n: int) -> int:
        if n<2:
            return 0
        
        soe = [ 1 ] * n
        # print(soe)
        soe[0]= 0
        soe[1]= 0
        
        for p in range(2, int(sqrt(n))+1):
            if soe[p]:
                for i in range(p*p,n,p):
                    soe[i]= 0
        
        # print(soe)
        return sum(soe)
        
        
        
