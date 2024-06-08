class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        rev_num = 0
        num = x

        while x != 0:
            rev = x % 10
            rev_num = rev_num * 10 + rev
            x //= 10
            
        if rev_num == num:
            return True
        else:
            return False

        
        