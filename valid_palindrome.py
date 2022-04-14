"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward and 
backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise

Examples - 

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

import re


class ValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        if not s or len(s) == 1: 
            return True
        s = re.findall("[a-zA-Z0-9]+", s)
        if s: s = ''.join(s).lower()
        return s == s[::-1]

if __name__ == "__main__":
    print(ValidPalindrome().isPalindrome("a23a213"))
