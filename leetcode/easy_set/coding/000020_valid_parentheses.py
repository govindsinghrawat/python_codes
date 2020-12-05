##########
#Question#
##########
'''
URL: https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''


##########
#Solution#
##########
class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = Stack()
        match_flag=True
        if len(s)<=0:
            return True
        
        if len(s)%2!=0:
            return False
        
        for i in range(0,len(s)):
            if self.is_open_symbol(s[i]):
                my_stack.push_to_stack(s[i])
            elif self.is_close_symbol(s[i]):
                ch = my_stack.pop_from_stack()
                if ch == -1:
                    return False
                if self.brackets_match(s[i], ch):
                    match_falg=True
                    continue
                else:
                    match_flag=False
                    break
        if my_stack.tos!=-1 or match_flag == False:
            return False
        else:
            return True
                

    def is_open_symbol(self, ch):
        if ch == "(" or ch =="{" or ch == "[":
            return True
        return False
    
    def is_close_symbol(self, ch):
        if ch == ")" or ch =="}" or ch == "]":
            return True
        return False
    
    def brackets_match(self,b,a):
        if (a == "(" and b==")") or (a=="{" and b=="}") or (a=="[" and b=="]"):
            return True
        return False
    
    
class Stack:
    def __init__(self):
        self.tos=-1
        self.stack = []
    
    def push_to_stack(self, ch):
        self.stack.append(ch)
        self.tos+=1
    
    def pop_from_stack(self):
        if self.is_empty():
            return -1
        ch = self.stack.pop(self.tos)
        self.tos-=1
        return ch
    
    def is_empty(self):
        if self.tos < 0:
            return True
        return False



###########
#Solution2#
###########

class Solution2:
    def isValid(self, s: str) -> bool:
        ps = '(){}[]'
        
        stk = []
        
        for c in s:
            if not stk:
                stk.append(ps.find(c))
            else:
                if ps.find(c) - stk[-1] == 1 and stk[-1] % 2 == 0:
                    stk.pop()
                else:
                    stk.append(ps.find(c))
                    
        return len(stk) == 0
