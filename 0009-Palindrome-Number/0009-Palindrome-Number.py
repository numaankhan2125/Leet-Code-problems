class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        reversed = s[::-1]
        if(s == reversed):
            return True
        else:
            return False
        