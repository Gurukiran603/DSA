class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        k=x
        rev=0
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x//=10
        if k==rev:
            return True
        else:
            return False
