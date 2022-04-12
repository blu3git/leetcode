"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""

class Palindrome:

    def is_palindrome(self, x):
        """
        Reverse half of the number and check if it is equal to the first half.
        This will save us from int overflow problem.
        For numbers with odd number as length, remove middle number by dividing
        by 10 as middle number will always be equal to itself in palindrome.
        Time complexity : O(\log_{10}(n))O(log 10(n)). We divided the input by 10 
        for every iteration
        Space complexity : O(1)
        """
        result = False
        if x < 0 or x % 10 == 0 or x == 0:
           return result
        elif x < 10 :
            result = True
            return result
        rev = 0
        while x > rev:
            rev = (rev*10) + (x%10)
            x = x/10
        if rev == x or x == rev/10:
            result = True
        return result
